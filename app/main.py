# app/main.py
import streamlit as st
from retriever import get_relevant_docs
from chatbot import query_biogpt


st.set_page_config(page_title="Pediatric Leukemia DSS", layout="wide")
st.title("🧬 Pediatric Leukemia Medical Assistant")

st.markdown("""
Ask any medical question related to pediatric leukemia.
""")

# Input field
user_query = st.text_input("💬 Your Question:")

if user_query:
    with st.spinner("🔎 Retrieving context and generating answer..."):
        docs = get_relevant_docs(user_query)
        answer = query_biogpt(user_query, docs)

    # Output
    st.markdown("### 🩺 Response")
    st.success(answer)

    # Show context (optional)
    with st.expander("📄 Show Retrieved Context"):
        for i, doc in enumerate(docs):
            st.markdown(f"**Chunk {i+1}:** {doc[:500]}...")

