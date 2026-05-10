from utils.pdf_extractor import extract_pdf_as_json

pdf_path = "sample_pdfs/sample.pdf"

result = extract_pdf_as_json(pdf_path)

print("\n===== MARKDOWN OUTPUT =====\n")
print(result["markdown"][:1000])

print("\n===== JSON OUTPUT =====\n")
print(result["json"])