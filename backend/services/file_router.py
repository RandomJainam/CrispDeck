from backend.services.pdf_service import extract_text
from backend.services.ppt_service import extract_ppt_text
from backend.services.docx_service import extract_docx_text

def extract_content(path):

    if path.endswith(".pdf"):
        return extract_text(path)

    elif path.endswith(".pptx"):
        return extract_ppt_text(path)

    elif path.endswith(".docx"):
        return extract_docx_text(path)

    else:
        raise ValueError(
            f"Unsupported file type: {path}"
        )