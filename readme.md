# Mini RAG Application (Gemini + Streamlit)
Hi, this readme is developed by gpt , I just made it understand about how my project works.
A production-style **Retrieval-Augmented Generation (RAG)** system that allows users to upload documents and ask context-aware questions using Google's Gemini LLM. The application performs semantic search over uploaded documents and generates grounded answers with citations and chat memory support.

---

## 🚀 Live Demo URL

👉 **Live App:** [https://mini-rag-gemini-3fabd7ffddttqhb9wdkrfk.streamlit.app/]([https://YOUR-DEPLOYED-STREAMLIT-URL](https://mini-rag-gemini-3fabd7ffddttqhb9wdkrfk.streamlit.app/))
👉 **GitHub Repo:** [https://github.com/72897/mini-rag-gemini](https://github.com/72897/mini-rag-gemini)
👉 **Resume:** [https://drive.google.com/file/d/19_pj8lsnp9PKMQcZ51wucB5b6SfLESnZ/view?usp=sharing](https://drive.google.com/file/d/19_pj8lsnp9PKMQcZ51wucB5b6SfLESnZ/view?usp=sharing)

---

## ✅ Features

* PDF and TXT document upload
* Automatic text chunking
* Sentence Transformer embeddings
* FAISS vector database for semantic search
* Gemini 3 Flash LLM integration
* Source-based answers with inline citations
* Multi-turn chat history (conversation memory)
* Streamlit interactive UI

---

## 🛠 Tech Stack

* **Frontend UI:** Streamlit
* **LLM:** Google Gemini 3 Flash
* **Embeddings:** Sentence Transformers (all-MiniLM-L6-v2)
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

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux

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

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

⚠ Important:

* Never push `.env` to GitHub
* Keep API keys private

---

## ▶ Run Application Locally

```bash
streamlit run app.py
```

App runs at:

```
http://localhost:8501
```

---

## 🧠 System Architecture

```
User Query
     ↓
Chat History Memory
     ↓
FAISS Vector Similarity Search
     ↓
Relevant Document Chunks
     ↓
Prompt Construction
     ↓
Gemini LLM
     ↓
Final Answer + Citations
```

---

## 📊 How The RAG Pipeline Works

1. User uploads PDF/TXT document
2. Document is chunked using RecursiveCharacterTextSplitter
3. Embeddings are generated using Sentence Transformers
4. Chunks are stored in FAISS vector database
5. User query performs semantic similarity search
6. Retrieved chunks + conversation history sent to Gemini
7. Gemini generates grounded response with citations

---

## 📌 Index Configuration (Track B Requirement)

### Vector Database Settings

* **Embedding Model:** all-MiniLM-L6-v2
* **Vector Store:** FAISS (Local)
* **Chunk Size:** 500 characters
* **Chunk Overlap:** 100 characters
* **Top-K Retrieval:** 3 chunks per query

---

## 📝 Remarks (Limits, Trade-offs, Future Improvements)

### Current Limitations

* Uses local FAISS instead of cloud vector DB
* Session memory resets on app reload
* No authentication layer
* Single document upload at a time

---

### Trade-offs

* Chose FAISS for simplicity and fast local testing
* Used Gemini Flash model for lower latency
* Streamlit selected for rapid UI development

---

### What I Would Improve Next

* Add reranking using cross-encoder models
* Implement hybrid search (keyword + vector)
* Support multi-document indexing
* Add persistent database storage
* Implement streaming responses
* Add user authentication

---

## 🎯 Use Cases

* Enterprise document Q&A systems
* Research assistant tools
* Knowledge base chatbots
* Customer support automation
* Internal document retrieval

---

## 👨‍💻 Author

**Kunal Singh**
Track B — AI Engineer Internship Assessment
