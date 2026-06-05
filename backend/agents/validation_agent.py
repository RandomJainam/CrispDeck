import json

class ValidationAgent:

    def run(self, flashcards_json):

        try:

            cleaned = flashcards_json.replace("```json", "")
            cleaned = cleaned.replace("```", "")
            cleaned = cleaned.strip()

            cards = json.loads(cleaned)

            seen = set()
            validated = []

            for card in cards:

                q = card["question"].strip()

                if q not in seen:

                    validated.append(card)
                    seen.add(q)

            return validated

        except Exception as e:

            print("Validation Error:", e)

            return []