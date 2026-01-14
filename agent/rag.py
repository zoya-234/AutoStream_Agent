import json
from pathlib import Path

KB_PATH = Path("data/knowledge_base.json")

def load_knowledge_base():
    with open(KB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

KB = load_knowledge_base()

def retrieve_answer(query: str) -> str:
    query = query.lower()

    pricing = KB["pricing"]
    policies = KB["policies"]

    if "price" in query or "pricing" in query or "plan" in query:
        return (
            "Here are AutoStream's plans:\n\n"
            f"Basic Plan: {pricing['basic']['price']}, "
            f"{pricing['basic']['limits']}, "
            f"{pricing['basic']['resolution']} resolution.\n\n"
            f"Pro Plan: {pricing['pro']['price']}, "
            f"{pricing['pro']['limits']}, "
            f"{pricing['pro']['resolution']} resolution, "
            "includes AI captions and priority support."
        )

    if "refund" in query:
        return policies["refund"]

    if "support" in query:
        return policies["support"]

    return "I can help with pricing, plans, and company policies."
