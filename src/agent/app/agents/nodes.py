from langchain.messages import ToolMessage, SystemMessage
from typing import Literal
from langgraph.graph import END


from src.agent.app.agents.state import AgentState
from src.agent.app.agents.prompts import prompt
from src.agent.app.agents.model import llm_with_tools, tools_by_name
# from src.app.core import 

def router(state: AgentState) -> Literal["tool_node", END]:
    """Router node to decide whether to call a tool or end the conversation"""
    last_message = state["messages"][-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tool_node"
    return END

def llm_call(state: AgentState) -> AgentState:
    """LLM decides whether to call a tool or not"""
    response = llm_with_tools.invoke(
            [
                SystemMessage(prompt)
            ] + state["messages"]
        )
    return {"messages": [response]}

def tool_node(state: AgentState):
    """call the tool with the required arguments"""
    result = []

    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        args = tool_call["args"]


        tool_result = tool.invoke(args)

        result.append(
            ToolMessage(
                content = tool_result),
                tool_calls_id = tool_call["id"]
        )   

    return {"messages": result}
    

