from backend.services.llm_service import ask_llm

response = ask_llm(
    "What is TCP/IP? Answer in one sentence."
)

print(response)