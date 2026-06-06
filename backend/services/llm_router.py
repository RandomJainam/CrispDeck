from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

MODEL_MAP = {
    "concept": "openai/gpt-oss-20b:free",
    "generation": "openai/gpt-oss-20b:free",
    "validation": "openai/gpt-oss-20b:free",
    "coverage": "openai/gpt-oss-20b:free"
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