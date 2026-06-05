from backend.services.pdf_service import extract_text

class ExtractionAgent:

    def run(self, pdf_path):

        text = extract_text(pdf_path)

        return text