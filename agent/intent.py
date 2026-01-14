from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


llm = ChatOllama(
    model="llama3:8b",
    temperature=0
)

intent_prompt = PromptTemplate.from_template("""
You are an intent classification system for a SaaS AI agent.

Classify the user message into ONE of the following intents:
- greeting
- product_inquiry
- high_intent

Definitions:
greeting → casual hello or small talk
product_inquiry → asking about pricing, features, plans, or policies
high_intent → user clearly wants to sign up, try, buy, or use the product

User message:
"{message}"

Return ONLY the intent label.
""")

def classify_intent(message: str) -> str:
    response = llm.invoke(intent_prompt.format(message=message))
    return response.content.strip().lower()
