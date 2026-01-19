import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

from utils.loader import load_document
from utils.chunker import chunk_documents
from utils.embedder import get_embedding_model
from utils.vector_store import create_vector_store

# Load env
load_dotenv()

# Gemini Config
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_NAME = "models/gemini-3-flash-preview"
model = genai.GenerativeModel(MODEL_NAME)

# Streamlit UI Config
st.set_page_config(page_title="Mini RAG App", layout="wide")

st.title("Mini RAG Application (Gemini)")
st.caption("RAG with Chat History + Context Memory")

# Initialize Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

uploaded_file = st.file_uploader("Upload PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:

    file_path = f"data/{uploaded_file.name}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Document uploaded successfully")

    # Load and chunk document
    documents = load_document(file_path)
    chunks = chunk_documents(documents)

    # Create Vector DB
    embedding_model = get_embedding_model()

    with st.spinner("Building vector database..."):
        db = create_vector_store(chunks, embedding_model)

    st.success("Vector database ready")

    # Chat UI
    st.subheader("Ask Questions From Document")

    user_question = st.text_input("Enter your question")

    if st.button("Ask") and user_question:

        # Retrieve relevant chunks
        with st.spinner("Retrieving relevant context..."):
            retrieved_docs = db.similarity_search(user_question, k=3)

        context_text = ""
        sources = []

        for i, doc in enumerate(retrieved_docs):
            context_text += f"\nSource {i+1}:\n{doc.page_content}\n"
            sources.append(doc.metadata.get("source", "Uploaded Document"))

        # Build chat history string
        history_text = ""
        for chat in st.session_state.chat_history:
            history_text += f"User: {chat['question']}\nAssistant: {chat['answer']}\n"

        # Final RAG Prompt
        prompt = f"""
You are a helpful AI assistant.

Use BOTH:
1) Previous conversation history
2) Retrieved document context

Conversation History:
{history_text}

Document Context:
{context_text}

Question:
{user_question}

Rules:
- Answer ONLY from provided document context
- Use conversation history for continuity
- If answer not found say: "Not found in document"
- Mention source numbers in answer
"""

        # Gemini Response
        with st.spinner("Generating answer..."):
            response = model.generate_content(prompt)

        answer_text = response.text

        # Save to chat history
        st.session_state.chat_history.append({
            "question": user_question,
            "answer": answer_text
        })

        # Display Current Answer
        st.subheader("Answer")
        st.write(answer_text)

        # Display Sources
        st.subheader("Sources Used")
        for i, src in enumerate(sources):
            st.write(f"Source {i+1}: {src}")

    # Display Chat History
    if st.session_state.chat_history:
        st.subheader("Conversation History")

        for i, chat in enumerate(reversed(st.session_state.chat_history)):
            st.markdown(f"### User {len(st.session_state.chat_history)-i}")
            st.write(chat["question"])
            st.markdown("### Assistant")
            st.write(chat["answer"])
