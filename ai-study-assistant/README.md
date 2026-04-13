# 🧠 AI Study Assistant

## 📌 Overview

AI Study Assistant is a web application that allows users to store notes and ask questions based on them.  
It uses a Retrieval-Augmented Generation (RAG) approach to retrieve relevant notes and generate answers.

---

## ⚙️ Architecture

```
User Input
   ↓
Streamlit App (app.py)
   ↓
RAG Pipeline (rag_pipeline.py)
   ↓
OpenRouter Embeddings
   ↓
NumPy + Endee (vector search)
   ↓
OpenRouter LLM
   ↓
Response to User
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

Endee is used as a supporting library for vector-based operations.  
Embeddings generated using OpenRouter are stored locally, and cosine similarity is applied using NumPy to retrieve the most relevant notes.

---

## ✨ Features

- Store and manage notes  
- Semantic search using embeddings  
- Context-based question answering  
- Notes summarization  
- Batch embedding for faster performance  
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
├── .gitignore
```

---

## 🚀 Setup

```bash
git clone https://github.com/Kalaiselvi-25/endee.git
cd ai-study-assistant
```

Create `.env` file:

```
OPENROUTER_API_KEY=your_api_key_here
```

Run locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Or with Docker:

```bash
docker-compose up
```

---

## 🚀 Usage

1. Paste notes  
2. Click **Store**  
3. Ask a question  
4. View answer and relevant notes  

---

## 🙌 Credits

- Endee: https://github.com/endee-io/endee  
- OpenRouter  
- Streamlit  