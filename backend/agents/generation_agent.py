from backend.services.llm_router import ask_llm

class GenerationAgent:

    def run(self, concepts):

        prompt = f"""
        You are an expert educator.

        Generate flashcards from these concepts.

        Rules:
        - Question should be clear.
        - Answer should be concise.
        - Return ONLY JSON.

        Format:

        [
            {{
                "question":"...",
                "answer":"..."
            }}
        ]

        Concepts:

        {concepts}
        """

        response = ask_llm(
            prompt,
            task="generation"
        )
    
        return response
    