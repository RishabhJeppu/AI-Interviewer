# Helper functions (parsing, formatting)
import PyPDF2
import docx
import os


def parse_resume(file_path: str) -> str:
    """
    Parses a PDF or DOCX file and returns the extracted text.

    :param file_path: Path to the document
    :return: Extracted text as a string
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    file_extension = file_path.lower().split(".")[1]

    if file_extension == "pdf":
        return parse_pdf(file_path)
    elif file_extension == "docx":
        return parse_docx(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")


def parse_pdf(file_path: str) -> str:
    """Extract text from a PDF file using PyPDF2."""
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += (
                page.extract_text() + "\n" if page.extract_text() else ""
            )  # Handle empty pages
    return text.strip()


def parse_docx(file_path: str) -> str:
    """Extract text from a DOCX file."""
    doc = docx.Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text.strip()
