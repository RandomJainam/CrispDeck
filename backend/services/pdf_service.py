import fitz

from backend.services.ocr_service import (
    extract_ocr_text
)

def extract_text(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:

        text += page.get_text()

    if text.strip():

        return text

    print(
        "No embedded text found. Running OCR..."
    )

    return extract_ocr_text(
        pdf_path
    )