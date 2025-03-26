# app/chatbot.py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load BioGPT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/BioGPT")
model = AutoModelForCausalLM.from_pretrained("microsoft/BioGPT")

def query_biogpt(user_query, context_docs):
    """Combine context and query into a prompt, generate a response using BioGPT."""
    prompt = "You are a medical assistant specialized in pediatric leukemia.\n\n"
    prompt += "Relevant context:\n"
    prompt += "\n---\n".join(context_docs)
    prompt += f"\n\nQuestion: {user_query}\nAnswer:"

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)
    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True).split("Answer:")[-1].strip()
