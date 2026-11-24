from io import BytesIO


def extract_text(name, data):
    """Plain text from an uploaded resume. name: file name, data: raw bytes."""
    name = name.lower()
    if name.endswith(".pdf"):
        from pypdf import PdfReader
        return "\n".join(page.extract_text() or "" for page in PdfReader(BytesIO(data)).pages)
    if name.endswith(".docx"):
        from docx import Document
        return "\n".join(p.text for p in Document(BytesIO(data)).paragraphs)
    if name.endswith(".txt"):
        return data.decode("utf-8", errors="replace")
    raise ValueError(f"Unsupported file type: {name}")
