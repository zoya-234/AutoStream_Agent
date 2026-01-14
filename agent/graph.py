from langgraph.graph import StateGraph
from langgraph.graph import END 
from agent.agent_logic import agent_step
from agent.state import AgentState

def agent_node(state: AgentState) -> AgentState:
    """
    Single LangGraph node that processes one turn.
    The user message is expected to be the last item in state["messages"].
    """
    user_message = state["messages"][-1]
    return agent_step(state, user_message)

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("agent", agent_node)

    # Entry point
    graph.set_entry_point("agent")

    # Loop until END is returned
    graph.add_edge("agent", END)

    return graph.compile()
