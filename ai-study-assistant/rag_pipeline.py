import streamlit as st
from endee_client import EndeeClient
import requests
import os
from dotenv import load_dotenv
import numpy as np

load_dotenv()

# 🔥 Cache DB (VERY IMPORTANT)
@st.cache_resource
def get_db():
    return EndeeClient()

db = get_db()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# 🔥 Simple embedding (NO sentence-transformers)
@st.cache_data
def get_embedding(text):
    return np.array([hash(text) % 1000 for _ in range(384)], dtype="float32")


# 🔹 Add notes
def add_notes(text):
    chunks = [c.strip() for c in text.split(".") if c.strip()]

    if not chunks:
        return

    embeddings = [get_embedding(chunk) for chunk in chunks]

    for emb, chunk in zip(embeddings, chunks):
        db.add(emb, chunk)


# 🔹 Retrieve relevant chunks
def retrieve(query):
    query_embedding = get_embedding(query)
    return db.search(query_embedding)


# 🔹 Generate answer (same as before)
def generate_answer(query, context):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        prompt = f"""
Answer based ONLY on this context:

{context}

Question: {query}
"""

        data = {
            "model": "meta-llama/llama-3-8b-instruct",
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=15
        )

        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"


# 🔹 Summarize notes (same as before)
def summarize_notes(text):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        prompt = f"Summarize into bullet points:\n{text}"

        data = {
            "model": "meta-llama/llama-3-8b-instruct",
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=15
        )

        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"