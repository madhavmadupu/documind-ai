from langchain.document_loaders import PyPDFLoader, TextLoader
from pathlib import Path

def load_document(path: str):
    suffix = Path(path).suffix.lower()

    if suffix == ".pdf":
        return PyPDFLoader(path).load()
    else:
        return TextLoader(path).load()
