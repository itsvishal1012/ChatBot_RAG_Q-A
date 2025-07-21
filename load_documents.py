import os
import pdfplumber
import docx
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import streamlit as st  # ✅ Needed for user-friendly warnings

# Load model and initialize FAISS
model = SentenceTransformer('all-MiniLM-L6-v2')
dimension = 384  # Embedding size for the model
index = faiss.IndexFlatL2(dimension)
documents = []  # Global document store

# Loaders for different file types
def load_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def load_pdf(file_path):
    pdf_text = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                pdf_text.extend([line.strip() for line in text.split('\n') if line.strip()])
    return pdf_text

def load_docx(file_path):
    doc = docx.Document(file_path)
    return [para.text.strip() for para in doc.paragraphs if para.text.strip()]

def load_xlsx(file_path):
    excel_text = []
    df = pd.read_excel(file_path)
    for column in df.columns:
        excel_text.extend([str(cell).strip() for cell in df[column] if pd.notnull(cell)])
    return excel_text

# General loader
def load_documents(file_path):
    global documents
    file_extension = os.path.splitext(file_path)[-1].lower()
    try:
        if file_extension == ".txt":
            documents.extend(load_txt(file_path))
        elif file_extension == ".pdf":
            documents.extend(load_pdf(file_path))
        elif file_extension == ".docx":
            documents.extend(load_docx(file_path))
        elif file_extension == ".xlsx":
            documents.extend(load_xlsx(file_path))
        else:
            st.warning(f"Unsupported file type: {file_extension}")
    except Exception as e:
        st.error(f"Failed to load {file_path}: {e}")

# Indexing function
def add_documents_to_index():
    global documents
    if not documents:
        st.warning("No documents to index. Please upload and load some documents.")
        return
    embeddings = model.encode(documents)
    index.add(np.array(embeddings, dtype=np.float32))

# Retrieval function with safety checks
def retrieve_relevant_documents(query, top_k=3):
    if not documents:
        st.warning("No documents available. Please upload files before querying.")
        return ["No documents uploaded."]

    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding, dtype=np.float32), top_k)

    retrieved_docs = []
    for idx in indices[0]:
        if idx < len(documents):
            retrieved_docs.append(documents[idx])
        else:
            st.warning(f"Index {idx} is out of range. Skipping.")
    return retrieved_docs
