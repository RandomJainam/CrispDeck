from backend.services.llm_router import ask_llm

class ConceptAgent:

    def run(self, text):

        prompt = f"""
        You are an academic content analyzer.

        Extract major concepts and topics.

        Return ONLY a clean bullet list.

        Content:

        {text[:12000]}
        """

        response = ask_llm(
            prompt,
            task="concept"
        )

        return response