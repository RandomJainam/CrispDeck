from backend.services.pdf_service import extract_text

text = extract_text(
    "backend/uploads/image(212) (1).pdf"
)

print(text)

print("\nLength:", len(text))