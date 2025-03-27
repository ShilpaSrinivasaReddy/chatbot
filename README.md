# Pediatric Leukemia DSS Chatbot

This is a Decision Support System (DSS) chatbot built to assist doctors with queries related to **pediatric leukemia**, using a combination of:

- **BioGPT** (medical language model from Microsoft)
- **RAG pipeline** (retrieves relevant medical documents)
- **Streamlit** (for the user interface)

---

## Features

- Natural language chatbot interface for medical queries
- Retrieves relevant context from pediatric leukemia literature
- Generates expert-style medical responses using BioGPT
- Web interface built using Streamlit

---

## Tech Stack

- Python 3.8+
- Hugging Face Transformers (`microsoft/BioGPT`)
- SentenceTransformers (`all-MiniLM-L6-v2`)
- FAISS (for vector similarity search)
- Streamlit (web UI)
- PyMuPDF (for parsing medical PDFs)

---

