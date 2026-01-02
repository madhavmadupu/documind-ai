import faiss
import numpy as np
from src.embeddings.embedding_manager import EmbeddingManager
from config.settings import settings

class VectorStore:
    def __init__(self):
        self.embedder = EmbeddingManager(settings.EMBEDDING_MODEL)
        self.index = faiss.IndexFlatL2(384)
        self.documents = []

    def add_documents(self, docs):
        texts = [d.page_content for d in docs]
        vectors = self.embedder.embed(texts)
        self.index.add(np.array(vectors).astype("float32"))
        self.documents.extend(docs)

    def search(self, query, k=5):
        q_vec = self.embedder.embed([query])
        _, idxs = self.index.search(
            np.array(q_vec).astype("float32"), k
        )
        return [self.documents[i] for i in idxs[0]]