from agent.graph import build_graph
from agent.state import AgentState

app = build_graph()

state: AgentState = {
    "messages": [],
    "intent": None,
    "name": None,
    "email": None,
    "platform": None,
    "lead_mode": False
}

print("AutoStream Agent (type 'exit' to quit)\n")

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    # Capture lead details if in lead mode
    if state["lead_mode"]:
        if state["name"] is None:
            state["name"] = user_input
        elif state["email"] is None:
            state["email"] = user_input
        elif state["platform"] is None:
            state["platform"] = user_input

    # Add user message to state
    state["messages"].append(user_input)

    # Run LangGraph
    state = app.invoke(state)

    print("Agent:", state["messages"][-1])
