from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

MODEL_MAP = {
    "concept": "openrouter/free",
    "generation": "openrouter/free",
    "validation": "openrouter/free",
    "coverage": "openrouter/free"
}

def ask_llm(prompt, task="generation"):

    model = MODEL_MAP.get(
        task,
        "deepseek/deepseek-chat-v4:free"
    )

  
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content