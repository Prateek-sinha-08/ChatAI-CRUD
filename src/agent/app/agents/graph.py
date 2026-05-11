from langgraph.graph import StateGraph, START, END
from langchain.messages import SystemMessage, HumanMessage, ToolMessage


from src.agent.app.agents.nodes import llm_call, tool_call
from src.agent.app.agents.state import AgentState

state = {"messages": []}

config = {"configurable": {"thread_id": "1"}}

from dotenv import load_dotenv
load_dotenv()

graph = StateGraph(AgentState)

graph.add_node("llm_call", llm_call)
graph.add_node("tool_call", tool_call)

graph.add_edge(START, "llm_call")
graph.add_edge("llm_call", "tool_call")
graph.add_edge("tool_call", "llm_call")
graph.add_edge("llm_call", END)

agent = graph.compile()

print("Finished compiling the agent")
