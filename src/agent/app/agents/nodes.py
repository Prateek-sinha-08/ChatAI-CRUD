from langchain_core.messages import ToolMessage, SystemMessage
from typing import Literal
from langgraph.graph import END
from sqlalchemy import select
from types import SimpleNamespace
import logging

from src.agent.app.agents.state import AgentState
from src.agent.app.agents.prompts import prompt
from src.agent.app.agents.model import llm_with_tools, tools_by_name
from src.agent.app.db.session import AsyncSessionLocal
from src.agent.app.models.user import User

log = logging.getLogger(__name__)

async def auth_node(state: AgentState):
    """This Node will fetch the username from the database and add it to the state, so that it can be given to the tools"""
    log.info(f"AUTH NODE STATE: {state}")
    user_id = state.get("user_id")
    log.info(f"Auth node: received user_id {user_id} in state {state}")
    if not user_id:
        return {**state, "username": None}
    
    async with AsyncSessionLocal() as db:
        try:
            db_user_id = int(user_id)
            result = await db.execute(
                select(User).where(User.id == db_user_id)
            )
        except (ValueError, TypeError):
            result = await db.execute(
                select(User).where(User.username == str(user_id))
            )

        
        user = result.scalar_one_or_none()
        log.info(f"Auth node: fetched user {user} for user_id {user_id}")
        if user:
            return {
                **state,
                "username": user.username}
        
        return {**state, "username": None}



def router(state: AgentState) -> Literal["tool_node", END]:
    """Router node to decide whether to call a tool or end the conversation"""
    last_message = state["messages"][-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tool_node"
    return END

def llm_call(state: AgentState) -> AgentState:
    """LLM decides whether to call a tool or not"""
    log.info(f"STATE ENTERING LLM NODE: {state}")
    response = llm_with_tools.invoke(
            [
                SystemMessage(prompt)
            ] + state["messages"]
        )
    return {
        **state,
        "messages": [response]}

def tool_node(state: AgentState):
    """call the tool with the required arguments"""
    log.info(f"STATE ENTERING TOOL NODE: {state}")
    result = []

    username = state.get("username")
    # user_context = SimpleNamespace(username=username) 
    # args["username"] = username

    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        args = tool_call["args"]

        args["user"] = username
        tool_result = tool.invoke(args)

        result.append(
            ToolMessage(
                content=str(tool_result)    ,
                tool_call_id=tool_call["id"],
            )
        )

    return {
        **state,
        "messages": result}
    

