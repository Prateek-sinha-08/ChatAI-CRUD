from langgraph.messages import ToolMessage, SystemMessage


from state import AgentState
from prompts import prompt
from model import llm_with_tools, tools_by_name
# from src.app.core import 

def llm_call(state: AgentState) -> AgentState:
    """LLM decides whether to call a tool or not"""
    response = llm_with_tools.invoke(
            [
                SystemMessage(prompt)
            ] + state["messages"]
        )
    return response

def tool_call(state: AgentState):
    """call the tool with the required arguments"""
    result = []

    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        args = tool_call["args"]


        tool_result = tool.invoke(args)

        result.append(
            ToolMessage(
                content = tool_result)
        )   

    return result
    

