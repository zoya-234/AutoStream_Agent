from langchain_ollama import ChatOllama
# from agent.rag import retrieve_answer
from agent.intent import classify_intent

llm = ChatOllama(
    model="llama3:8b",
    temperature=0
)

response = llm.invoke("Say hello in one sentence")
print(response.content)

# print(retrieve_answer("Tell me about pricing"))
# print(retrieve_answer("What is your refund policy?"))

tests = [
    "Hi there!",
    "Can you tell me about your pricing?",
    "I want to try the Pro plan for my YouTube channel"
]

for t in tests:
    print(t, "→", classify_intent(t))