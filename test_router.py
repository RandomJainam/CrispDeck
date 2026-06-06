from backend.services.llm_router import ask_llm

print(
    ask_llm(
        "What is TCP/IP in one sentence?",
        task="concept"
    )
)