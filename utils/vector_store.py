from langchain_community.vectorstores import FAISS
import os

VECTOR_DB_PATH = "vector_store"

def create_vector_store(chunks, embedding_model):
    db = FAISS.from_documents(chunks, embedding_model)
    db.save_local(VECTOR_DB_PATH)
    return db

def load_vector_store(embedding_model):
    if os.path.exists(VECTOR_DB_PATH):
        return FAISS.load_local(VECTOR_DB_PATH, embedding_model)
    else:
        return None
