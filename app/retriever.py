# app/retriever.py
import os
import pickle
from sentence_transformers import SentenceTransformer
import faiss

# Get path relative to project root
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
embedding_path = os.path.join(base_path, "embeddings", "docs.pkl")

model = SentenceTransformer("all-MiniLM-L6-v2")

with open(embedding_path, "rb") as f:
    index, chunks = pickle.load(f)

def get_relevant_docs(query, top_k=3):
    query_embedding = model.encode([query])
    D, I = index.search(query_embedding, top_k)
    return [chunks[i] for i in I[0]]
