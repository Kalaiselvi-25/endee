import streamlit as st
from endee_client import EndeeClient
import requests
import os
from dotenv import load_dotenv
import numpy as np

load_dotenv()

# 🔥 Cache DB
@st.cache_resource
def get_db():
    return EndeeClient()

db = get_db()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# ==============================
# 🔥 BATCH EMBEDDINGS (FAST 🚀)
# ==============================
@st.cache_data
def get_embeddings(texts):
    url = "https://openrouter.ai/api/v1/embeddings"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "text-embedding-3-small",
        "input": texts
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    return [np.array(item["embedding"], dtype="float32") for item in result["data"]]


# 🔹 Single embedding (for query only)
@st.cache_data
def get_embedding(text):
    return get_embeddings([text])[0]


# ==============================
# 🔹 ADD NOTES (OPTIMIZED)
# ==============================
def add_notes(text):
    # Limit chunks → faster
    chunks = [c.strip() for c in text.split(".") if c.strip()][:10]

    if not chunks:
        return

    # 🚀 ONE API CALL instead of many
    embeddings = get_embeddings(chunks)

    for emb, chunk in zip(embeddings, chunks):
        db.add(emb, chunk)


# ==============================
# 🔹 RETRIEVE
# ==============================
def retrieve(query):
    query_embedding = get_embedding(query)
    return db.search(query_embedding)


# ==============================
# 🔹 GENERATE ANSWER
# ==============================
def generate_answer(query, context):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        prompt = f"""
Answer ONLY using the context below.

Context:
{context}

Question: {query}

If the answer is not in the context, say:
"I don't know based on the provided notes."
"""

        data = {
            "model": "meta-llama/llama-3-8b-instruct",
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=20
        )

        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"


# ==============================
# 🔹 SUMMARIZE
# ==============================
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
            timeout=20
        )

        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"