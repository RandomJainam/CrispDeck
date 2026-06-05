from backend.services.llm_service import ask_llm

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

        return ask_llm(prompt)