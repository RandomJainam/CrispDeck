import fitz
import easyocr
import tempfile
import os

reader = easyocr.Reader(
    ["en"],
    gpu=False
)

def extract_ocr_text(pdf_path):

    doc = fitz.open(pdf_path)

    full_text = ""

    for page_num in range(len(doc)):

        page = doc.load_page(page_num)

        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)

        with tempfile.NamedTemporaryFile(
            suffix=".png",
            delete=False
        ) as temp_file:

            img_path = temp_file.name

        pix.save(img_path)

        result = reader.readtext(
            img_path,
            detail=0
        )

        os.remove(img_path)

        page_text = "\n".join(result)

        full_text += (
            page_text + "\n\n"
        )

    return full_text