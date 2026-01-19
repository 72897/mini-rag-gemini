# Mini RAG Application (Gemini + Streamlit)

A production-style **Retrieval-Augmented Generation (RAG)** system that allows users to upload documents and ask context-aware questions using Google's Gemini LLM. The application performs semantic search over uploaded documents and generates grounded answers with citations and chat memory support.

---

## 🚀 Features

* PDF and TXT document upload
* Automatic text chunking
* Sentence Transformer embeddings
* FAISS vector database for semantic search
* Gemini 3 Flash LLM integration
* Source-based answers with citations
* Multi-turn chat history (conversation memory)
* Streamlit interactive web interface

---

## 🛠 Tech Stack

* **Frontend UI:** Streamlit
* **LLM:** Google Gemini 3 Flash
* **Embeddings:** Sentence Transformers
* **Vector Database:** FAISS
* **Framework:** LangChain
* **Programming Language:** Python

---

## 📁 Project Structure

```
mini-rag-gemini
│
├── app.py
├── requirements.txt
├── .env
├── data/
├── vector_store/
├── utils/
│   ├── __init__.py
│   ├── loader.py
│   ├── chunker.py
│   ├── embedder.py
│   └── vector_store.py
└── README.md
```

---

## ⚙ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone <your-github-repo-url>
cd mini-rag-gemini
```

---

### 2️⃣ Create Virtual Environment

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Create a `.env` file in root directory:

```
GEMINI_API_KEY=your_api_key_here
```

⚠ Important:

* Do NOT push `.env` file to GitHub
* Keep API key private

---

## ▶ Run Application

Start Streamlit server:

```bash
streamlit run app.py
```

Application will be available at:

```
http://localhost:8501
```

---

## 📊 How The System Works

1. User uploads PDF or TXT document
2. Document is split into chunks
3. Embeddings are generated using Sentence Transformers
4. Vectors stored in FAISS database
5. User query triggers semantic similarity search
6. Retrieved chunks + chat history sent to Gemini
7. Gemini generates grounded response with citations

---

## 🧠 RAG Pipeline Architecture

```
User Query
     ↓
Chat History Memory
     ↓
Vector Similarity Search (FAISS)
     ↓
Relevant Context Retrieval
     ↓
Prompt Injection
     ↓
Gemini LLM
     ↓
Final Answer + Citations
```

---

## 🎯 Use Cases

* Enterprise document Q&A
* Research assistants
* Knowledge base chatbots
* Customer support automation
* Internal document search tools

---

## 📌 Key Highlights

* Prevents hallucinations using context grounding
* Supports follow-up questions via conversation memory
* Lightweight local vector storage
* Easy cloud deployment
* Internship assessment ready

---

## 👨‍💻 Author

**Kunal Singh**
Track B — AI Engineer Internship Assessment

---

## ⭐ Future Improvements (Optional)

* Hybrid search (keyword + vector)
* Reranking with Cross Encoders
* Multi-file indexing
* Streaming LLM responses
* Authentication layer
* Cloud vector database integration
