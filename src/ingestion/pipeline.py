import time
from .loaders import load_document
from .chunking import chunk_documents
from src.retrieval.vector_store import VectorStore

class IngestionPipeline:
    def __init__(self):
        self.vector_store = VectorStore()

    def ingest_file(self, path: str, metadata=None):
        start = time.time()
        docs = load_document(path)
        chunks = chunk_documents(docs)

        self.vector_store.add_documents(chunks)

        return {
            "success": True,
            "file_path": path,
            "num_chunks": len(chunks),
            "processing_time_seconds": round(time.time() - start, 2)
        }