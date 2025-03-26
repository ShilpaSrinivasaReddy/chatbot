import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.retriever import get_relevant_docs
from app.chatbot import query_biogpt

query = "What are common symptoms of pediatric leukemia?"

docs = get_relevant_docs(query)
response = query_biogpt(query, docs)

print("📘 Retrieved Context:")
for d in docs:
    print(d[:300], "\n---")

print("\n💬 Response from BioGPT:")
print(response)
