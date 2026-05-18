from langgraph.graph import StateGraph, START, END
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage


from src.agent.app.agents.nodes import auth_node, llm_call, router, tool_node
from src.agent.app.agents.state import AgentState

state = {"messages": []}

config = {"configurable": {"thread_id": "1"}}

from dotenv import load_dotenv
load_dotenv()

graph = StateGraph(AgentState)

graph.add_node("auth_node", auth_node)
graph.add_node("llm_call", llm_call)
graph.add_node("tool_node", tool_node)

graph.add_edge(START, "auth_node")
graph.add_edge("auth_node", "llm_call")

graph.add_conditional_edges(
    "llm_call", # source node
    router,  # routing function that decides the next node based on the state
    ["tool_node", END]  # possible target nodes based on the router's return value
)

graph.add_edge("tool_node", "llm_call")

agent = graph.compile(debug = True)

print("Finished compiling the agent")
