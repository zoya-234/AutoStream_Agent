from langchain_core.prompts import PromptTemplate
from agent.llm import get_llm

llm = get_llm()

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
