import streamlit as st
import os
from utils.pdf_extractor import extract_pdf_as_json

st.set_page_config(
    page_title="PDF Compliance Scanner",
    layout="wide"
)

st.title("📄 GenAI PDF Compliance Scanner")

st.write("""
Upload a PDF and run compliance checks using Generative AI.
""")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

if uploaded_file:

    save_path = os.path.join(
        "sample_pdfs",
        uploaded_file.name
    )
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Saved PDF to: {save_path}")

if st.button("Run Compliance Scan"):
    with st.spinner("Scanning PDF..."):
        result = extract_pdf_as_json(save_path)
        st.subheader("Markdown Preview")
        st.text(result["markdown"][:3000])