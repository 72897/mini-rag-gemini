from langchain_community.document_loaders import PyPDFLoader, TextLoader
import os

def load_document(file_path):
    ext = os.path.splitext(file_path)[1]

    if ext == ".pdf":
        loader = PyPDFLoader(file_path)
    elif ext == ".txt":
        loader = TextLoader(file_path)
    else:
        raise ValueError("Unsupported file format")

    documents = loader.load()
    return documents
