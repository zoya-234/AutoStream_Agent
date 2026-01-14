from langchain_ollama import ChatOllama
# from agent.rag import retrieve_answer
# from agent.intent import classify_intent
from agent.agent_logic import agent_step
from agent.state import AgentState


llm = ChatOllama(
    model="llama3:8b",
    temperature=0
)

response = llm.invoke("Say hello in one sentence")
print(response.content)

# print(retrieve_answer("Tell me about pricing"))
# print(retrieve_answer("What is your refund policy?"))

# tests = [
#     "Hi there!",
#     "Can you tell me about your pricing?",
#     "I want to try the Pro plan for my YouTube channel"
# ]

# for t in tests:
#     print(t, "→", classify_intent(t))

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

    # Capture user-provided details
    if state["lead_mode"]:
        if state["name"] is None:
            state["name"] = user_input
        elif state["email"] is None:
            state["email"] = user_input
        elif state["platform"] is None:
            state["platform"] = user_input
    state = agent_step(state, user_input)
    print("Agent:", state["messages"][-1])