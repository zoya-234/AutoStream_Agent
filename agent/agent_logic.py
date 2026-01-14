from agent.intent import classify_intent
from agent.rag import retrieve_answer
from agent.tools import mock_lead_capture
from agent.state import AgentState

def agent_step(state: AgentState, user_message: str) -> AgentState:
    state["messages"].append(user_message)

    # 🔒 If lead mode is active, DO NOT reclassify intent
    if state["lead_mode"]:
        if not state["name"]:
            state["messages"].append("Great! May I know your name?")
            return state

        if not state["email"]:
            state["messages"].append("Thanks! Could you share your email address?")
            return state

        if not state["platform"]:
            state["messages"].append(
                "Which platform do you create content on? (YouTube, Instagram, etc.)"
            )
            return state

        # ✅ All info collected → tool call
        mock_lead_capture(
            state["name"],
            state["email"],
            state["platform"]
        )

        state["messages"].append(
            "You're all set! Our team will contact you shortly 🚀"
        )

        state["lead_mode"] = False  # reset after completion
        return state

    # 🧠 Normal intent classification
    intent = classify_intent(user_message)
    state["intent"] = intent

    if intent == "greeting":
        state["messages"].append("Hi! How can I help you with AutoStream?")
        return state

    if intent == "product_inquiry":
        answer = retrieve_answer(user_message)
        state["messages"].append(answer)
        return state

    if intent == "high_intent":
        state["lead_mode"] = True
        state["messages"].append("Great! May I know your name?")
        return state

    return state
