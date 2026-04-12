# 🧠 AI Study Assistant

## 📌 Project Overview

The **AI Study Assistant** is a web-based application that helps users store, manage, and retrieve study notes intelligently. Users can input notes and ask questions, and the system returns relevant answers based on the stored content.

The project follows a **Retrieval-Augmented Generation (RAG)** approach:
- Notes are converted into vector embeddings  
- Relevant notes are retrieved using similarity search  
- Answers are generated based on retrieved context  

### 🎯 Problem it Solves

Students often struggle to:
- Organize large volumes of notes  
- Quickly find relevant information  
- Get concise answers from their own study material  

This project provides a **smart assistant** that improves study efficiency.

---

## 🏗️ System Design / Architecture

```
User Input (Notes / Questions)
        ↓
Streamlit Web App
        ↓
Embedding Generation 
        ↓
Endee Vector Database
        ↓
Similarity Search
        ↓
LLM (OpenRouter API - optional)
        ↓
Response to User
```

---

## 🛠️ Tech Stack

- **Frontend & App Framework**: Streamlit  
- **Backend Logic**: Python  
- **Vector Database**: Endee (custom integration)  
- **Embeddings**: NumPy (lightweight embedding approach)  
- **LLM API**: OpenRouter (LLaMA 3 model)  
- **Environment Variables**: python-dotenv  
- **Containerization**: Docker, Docker Compose  

---

## 🧠 How Endee is Used

Endee is used as the **vector database layer** in this project.

### Integration Details:
- Notes are converted into embeddings  
- Embeddings and corresponding text are stored locally  
- Data is persisted using a `.pkl` file  
- During query:
  - Query is converted into embedding  
  - Similarity is calculated  
  - Top matching notes are retrieved  

### Key Operations:
- `add()` → Store embeddings and text  
- `search()` → Retrieve similar notes  
- `clear()` → Reset stored data  

This enables efficient **semantic search over notes**.

---

## ✨ Features

- 📚 Store study notes  
- 🔍 Semantic search using vector similarity  
- 🤖 AI-based answer generation (optional via OpenRouter)  
- 📝 Note summarization  
- ⚡ Lightweight and fast  
- 🐳 Docker support  
- 💾 Persistent local storage  

---

## 📂 Project Structure

```
ai-study-assistant/
│
├── app.py
├── rag_pipeline.py
├── endee_client.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── .gitignore
└── endee_data.pkl
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-study-assistant.git
cd ai-study-assistant
```

### 2. Create `.env` file

```env
OPENROUTER_API_KEY=your_api_key_here
```

### 3. Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

### 4. Run with Docker

```bash
docker-compose up --build
```

---

## 🚀 Usage

1. Paste notes in the sidebar  
2. Click **Store**  
3. Ask a question  
4. View generated answers and relevant notes  

### Example

**Input Notes:**
```
Cloud computing provides services over the internet. Public cloud is shared. Private cloud is secure.
```

**Question:**
```
What is cloud computing?
```

**Output:**
```
Cloud computing is the delivery of computing services over the internet.
```

---

## 🔌 API Reference

- `add_notes(text)` → Store notes  
- `retrieve(query)` → Get relevant notes  
- `generate_answer(query, context)` → Generate answer  
- `summarize_notes(text)` → Summarize notes  

---

## 🔮 Future Improvements

- PDF upload support  
- Integration of advanced embedding models  
- Faster vector search optimization  
- User authentication system  
- Cloud deployment  

---

## 🙌 Acknowledgements

- **Endee Vector Database**: https://github.com/endee-io/endee  
- **Streamlit** for UI development  
- **OpenRouter** for LLM access  

---

## 📄 License

This project is licensed under the MIT License.