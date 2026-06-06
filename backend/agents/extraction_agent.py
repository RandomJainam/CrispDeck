from backend.services.file_router import extract_content

class ExtractionAgent:

    def run(self, file_path):

        return extract_content(file_path)