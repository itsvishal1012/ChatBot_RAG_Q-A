
# 📄 RAG-based Document Q&A ChatBot

This project is a **Streamlit-based chatbot application** that allows users to upload documents and interact with them using a conversational interface powered by **Google Gemini**. It leverages **RAG (Retrieval-Augmented Generation)** to retrieve relevant chunks of your uploaded documents and generate intelligent responses.

---

## 🚀 Features

- Upload and parse `.txt`, `.pdf`, `.docx`, `.xlsx` documents
- Retrieve the most relevant content using **FAISS** and **Sentence Transformers**
- Chat interface with Google Gemini API for intelligent response generation
- Clean dark-themed user interface
- History-aware conversations with document context

---

## 🧱 Project Structure

```
├── app.py                # Main Streamlit application
├── gemini.py             # Handles interaction with Google Gemini
├── load_documents.py     # Document loaders, embedding, FAISS index, and retrieval
├── utils.py              # Loads environment variables
├── requirements.txt      # Python dependencies
```

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/itsvishal1012/ChatBot_RAG_Q-A.git
cd ChatBot_RAG_Q-A
```

### 2. Create & Activate a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_google_generativeai_api_key
```

> 🔐 Don’t expose this file in public repositories.

### 5. Run the App

```bash
streamlit run app.py
```

---

## 🧠 How It Works

### Uploading Documents
- Users can upload documents in the sidebar.
- The files are read using respective parsers (`pdfplumber`, `docx`, `pandas`) and stored globally.

### Embedding & Indexing
- All loaded document text is encoded using the `all-MiniLM-L6-v2` model from SentenceTransformers.
- A FAISS index is built for fast nearest-neighbor search on query embeddings.

### Query Handling
- User inputs are embedded and compared to document vectors via FAISS.
- Top-matching snippets are retrieved and passed along with user history to the Google Gemini model for response generation.

---

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io/)
- [SentenceTransformers](https://www.sbert.net/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [pdfplumber](https://github.com/jsvine/pdfplumber)
- [python-docx](https://python-docx.readthedocs.io/)
- [pandas](https://pandas.pydata.org/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## 📎 Example Query

> Upload a PDF report, then ask:
> 
> **"Summarize the key points from the executive summary section."**

The app will retrieve the most relevant content and Gemini will generate a concise answer.

---

## ✅ TODOs

- [ ] Add support for more file types
- [ ] Improve chunking of large documents
- [ ] Add session saving and export history
- [ ] Enable Gemini Pro Vision for file-level insights

---

## 📄 License

