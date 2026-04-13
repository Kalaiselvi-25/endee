# 🧠 AI Study Assistant

A simple AI-powered web application to store notes and ask questions based on them using a Retrieval-Augmented Generation (RAG) approach.

---

## 📌 Overview

The AI Study Assistant helps users manage and understand their notes more effectively.  
It retrieves relevant information from stored notes and generates answers using an LLM.

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

<p>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Endee-000000?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenRouter-000000?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
</p>

---

## 🧠 Use of Endee

Endee is used as a supporting library for vector-based operations.  
Embeddings generated via OpenRouter are stored locally, and cosine similarity is applied using NumPy to retrieve relevant notes.

---

## ✨ Features

- 📚 Store and manage notes  
- 🔍 Semantic search using embeddings  
- 🤖 Context-based question answering  
- 📝 Notes summarization  
- ⚡ Batch embedding for faster performance  
- 🐳 Docker support  

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

### 1. Clone the repository

```bash
git clone https://github.com/Kalaiselvi-25/endee.git
cd ai-study-assistant
```

### 2. Configure environment

Create a `.env` file:

```
OPENROUTER_API_KEY=your_api_key_here
```

### 3. Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

### 4. Run with Docker

```bash
docker-compose up
```

---

## 🚀 Usage

1. Paste your notes  
2. Click **Store**  
3. Ask a question  
4. View answers and relevant notes  

---

## 🙌 Credits

- Endee — https://github.com/endee-io/endee  
- OpenRouter  
- Streamlit  
