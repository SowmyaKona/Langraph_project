from langgraph.graph import StateGraph, START, END
from models.state import AgentState

from agents.classifier_agent import classifier_node
from agents.policy_agent import policy_node
from agents.graph_agent import graph_node
from agents.response_agent import response_node

# Router Function
def router(state: AgentState):
    return state["route"]

# Graph
builder = StateGraph(AgentState)

# Nodes
builder.add_node("classifier", classifier_node)
builder.add_node("policy", policy_node)
builder.add_node("graph", graph_node)
builder.add_node("response", response_node)

# Edges
builder.add_edge(START, "classifier")
builder.add_conditional_edges("classifier",router,
    {
        "policy": "policy",
        "graph": "graph",
    }
)

builder.add_edge("policy","response")
builder.add_edge("policy","response")
builder.add_edge("response",END)

graph = builder.compile()