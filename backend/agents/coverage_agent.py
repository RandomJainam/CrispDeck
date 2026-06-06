from backend.services.llm_router import ask_llm
import json

class CoverageAgent:

    def run(self, syllabus_text, study_material_text):

        prompt = f"""
You are a syllabus coverage analyzer.

SYLLABUS:

{syllabus_text[:10000]}

STUDY MATERIAL:

{study_material_text[:15000]}

For every syllabus topic determine:

Covered
Partially Covered
Missing

Return ONLY valid JSON.

Example:

[
    {{
        "topic":"TCP/IP",
        "status":"Covered"
    }},
    {{
        "topic":"DNS",
        "status":"Partial"
    }}
]
"""

        response = ask_llm(
            prompt,
            task="coverage"
        )

        try:
            print(response)
            return json.loads(response)

        except:
            return []