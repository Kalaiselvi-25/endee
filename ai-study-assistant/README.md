# 🧠 AI Study Assistant

An AI-powered application that allows users to store notes, perform semantic search, and generate context-aware answers using a Retrieval-Augmented Generation (RAG) pipeline.

---

## 📌 Overview

AI Study Assistant helps users organize notes and quickly get answers from them.  
It retrieves relevant information using embeddings and generates responses using an LLM.

---

## ⚙️ System Architecture

```
1. User Input (Notes / Question)
        ↓
2. Streamlit UI
        ↓
3. RAG Pipeline
        ↓
4. Embedding Generation (OpenRouter)
        ↓
5. Vector Storage (Local + EndeeClient)
        ↓
6. Semantic Search (Cosine Similarity)
        ↓
7. LLM Response (OpenRouter)
        ↓
8. Output (Answer + Relevant Notes)
```




## 🛠️ Tech Stack

- Streamlit  
- Python  
- Endee (library integration)  
- NumPy (similarity computation)  
- OpenRouter API (Embeddings + LLM)  
- Docker  

---

## 🧠 Use of Endee

Endee is used as a supporting library for vector operations.  
Embeddings generated using OpenRouter enable semantic search, and similarity is used to retrieve relevant notes.

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
git clone https://github.com/username/endee.git
cd endee/ai-study-assistant
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
