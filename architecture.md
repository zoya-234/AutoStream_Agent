user
 ↓
Intent Classifier (LLM)
 ↓
┌───────────────┬─────────────────┬────────────────────┐
│ Casual Intent │ Product Inquiry │ High-Intent Lead   │
│ Greeting      │ RAG Answering   │ Lead Qualification │
└───────────────┴─────────────────┴────────────────────┘
                                      ↓
                              Tool Execution
                              (mock_lead_capture)
