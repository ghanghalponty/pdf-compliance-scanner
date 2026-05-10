import pymupdf4llm


def extract_pdf_as_json(pdf_path):
    """
    Extract PDF into structured LLM-ready JSON using PyMuPDF4LLM.

    Args:
        pdf_path (str): Path to PDF file

    Returns:
        dict: Structured document output (page-wise JSON/markdown)
    """

    # Convert PDF into structured Markdown (LLM-friendly)
    markdown_text = pymupdf4llm.to_markdown(pdf_path)

    # Also generate structured JSON-like output
    json_output = pymupdf4llm.to_json(pdf_path)

    return {
        "markdown": markdown_text,
        "json": json_output
    }