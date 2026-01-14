Here is your text converted to Markdown format:

**AutoStream – Social-to-Lead Agentic Workflow**
### Project Overview
#### This project implements a Conversational AI Agent for a fictional SaaS company AutoStream, which provides automated video editing tools for content creators.

The agent is designed to convert user conversations into qualified business leads, closely mirroring the Inflx Social-to-Lead agentic workflow described in the assignment.

Unlike a simple chatbot, this agent:

* Understands user intent
* Answers questions using a knowledge base (RAG)
* Identifies high-intent users
* Collects lead details across multiple turns
* Triggers a backend tool only when all conditions are met

#### Key Capabilities

1. **Intent Identification**

The agent classifies each user message into one of the following intents:

* Greeting
* Product Inquiry
* High Intent

Intent classification is performed using an LLM to ensure semantic understanding, not keyword matching.

2. **RAG-Powered Knowledge Retrieval**

The agent answers questions using a local knowledge base stored in a JSON file.

Knowledge includes:

* Pricing plans (Basic & Pro)
* Features
* Company policies (refunds, support)

This prevents hallucination and ensures answers are grounded in structured data.

3. **Stateful Lead Qualification**

When a user shows high intent, the agent:

* Locks into lead capture mode
* Collects:
	+ Name
	+ Email
	+ Creator platform
* Retains memory across multiple turns
* Triggers the lead capture tool only after all details are collected

4. **Tool Execution (Mock API)**

Once all required information is gathered, the agent calls a mock backend function:

```python
def mock_lead_capture(name, email, platform):
    print(f"Lead captured successfully: {name}, {email}, {platform}")
```

This simulates real-world CRM or backend integration.

#### Architecture Explanation

This project uses LangGraph to implement a deterministic, stateful agent workflow. LangGraph was chosen because it allows agent behavior to be modeled as a state machine, ensuring controlled execution and preventing unintended tool calls. Each user interaction triggers exactly one graph execution, making the system predictable and debuggable.

The agent maintains an explicit conversation state containing the message history, detected intent, lead details (name, email, platform), and a lead-lock flag. This state persists across 5–6 conversation turns, enabling the agent to reason over past interactions and safely manage multi-step lead qualification.

Retrieval-Augmented Generation (RAG) is implemented using a local JSON knowledge base that stores pricing and policy information. User queries are first matched against this knowledge source, and only the retrieved information is used to generate responses. This ensures accuracy and eliminates hallucination.

Once high intent is detected, the agent enters a locked lead-capture mode, preventing regression into greeting or product inquiry paths. Tool execution is strictly gated and only occurs when all required lead details are available, closely reflecting real-world production agent behavior.

The LLM backend is provided via Ollama, allowing local, cost-free inference while keeping the agent logic LLM-agnostic.

#### Tech Stack

* Language: Python 3.9+
* Agent Framework: LangGraph + LangChain
* LLM: Ollama (LLaMA 3)
* Knowledge Base: Local JSON (RAG)
* State Management: Typed agent state dictionary

### How to Run Locally

1. **Clone the Repository**
```bash
git clone <your-repo-url>
cd AutoStream_Agent
```

2. **Create Virtual Environment**
```python
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Start Ollama**

Ensure Ollama is running and the model is available:
```bash
ollama pull llama3:8b
```

5. **Run the Agent**
```python
python main.py
```

### Example Conversation Flow

User: Hi
Agent: Hi! How can I help you with AutoStream?

User: Tell me about pricing
Agent: (Pricing details)

User: I want to try the Pro plan
Agent: Great! May I know your name?

User: Zoya
Agent: Thanks! Could you share your email address?

User: zoya@email.com
Agent: Which platform do you create content on?

User: YouTube
Agent: You're all set! Our team will contact you shortly 🚀

### WhatsApp Integration (Design Explanation)

To deploy this agent on WhatsApp:

* Use the WhatsApp Business API
* Configure a Webhook (FastAPI/Flask) to receive incoming messages
* Map each WhatsApp user ID to an agent state (stored in Redis or a database)
* Forward user messages to the LangGraph agent
* Send agent responses back via the WhatsApp API

This allows persistent, real-time social-to-lead automation across conversations, aligning directly with Inflx’s use case.