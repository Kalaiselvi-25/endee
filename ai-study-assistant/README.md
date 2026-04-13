# 🧠 AI Study Assistant

A simple AI-powered web app to store notes and ask questions using a Retrieval-Augmented Generation (RAG) approach.

---

## 📌 Overview

AI Study Assistant helps users organize notes and quickly get answers from them.  
It retrieves relevant information using embeddings and generates responses using an LLM.

---

## ⚙️ Architecture

```
User Input
   ↓
Streamlit UI
   ↓
RAG Pipeline
   ↓
OpenRouter Embeddings
   ↓
Vector Search (NumPy + Endee)
   ↓
OpenRouter LLM
   ↓
Response
```

---

## 🛠️ Tech Stack

- Streamlit  
- Python  
- Endee (library integration)  
- NumPy (vector operations)  
- OpenRouter API (Embeddings + LLM)  
- Docker  

---

## 🧠 Use of Endee

Endee is used as a supporting library for vector operations.  
Embeddings are stored locally and cosine similarity (NumPy) is used to retrieve relevant notes.

---

## ✨ Features

- Store and manage notes  
- Semantic search using embeddings  
- Context-based question answering  
- Notes summarization  
- Docker support  

---

## 📂 Project Structure

```
ai-study-assistant/
├── app.py
├── rag_pipeline.py
├── endee_client.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .gitignore
```

---

## 🚀 Setup

```bash
git clone https://github.com/Kalaiselvi-25/endee.git
cd ai-study-assistant
```

Create `.env`:

```
OPENROUTER_API_KEY=your_api_key_here
```

Run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Or:

```bash
docker-compose up
```

---

## 🚀 Usage

1. Paste notes  
2. Click **Store**  
3. Ask a question  
4. View answers and relevant notes  

---

## 🙌 Credits

- Endee — https://github.com/endee-io/endee  
- OpenRouter  
- Streamlit  
