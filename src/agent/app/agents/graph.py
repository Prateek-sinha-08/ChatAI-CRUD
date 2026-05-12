from langgraph.graph import StateGraph, START, END
from langchain.messages import SystemMessage, HumanMessage, ToolMessage


from src.agent.app.agents.nodes import llm_call, router, tool_node
from src.agent.app.agents.state import AgentState

state = {"messages": []}

config = {"configurable": {"thread_id": "1"}}

from dotenv import load_dotenv
load_dotenv()

graph = StateGraph(AgentState)

graph.add_node("llm_call", llm_call)
graph.add_node("tool_node", tool_node)

graph.add_edge(START, "llm_call")
# graph.add_edge("llm_call", "tool_node")

graph.add_conditional_edges(
    "llm_call", # source node
    router,  # routing function that decides the next node based on the state
    ["tool_node", END]  # possible target nodes based on the router's return value
)

graph.add_edge("tool_node", "llm_call")

agent = graph.compile()

print("Finished compiling the agent")
