from .llm_manager import get_llm
from .prompts import RAG_PROMPT
from src.retrieval.vector_store import VectorStore

class RAGChain:
    def __init__(self):
        self.llm = get_llm()
        self.store = VectorStore()

    def query(self, question, top_k=5, include_sources=True, filters=None):
        docs = self.store.search(question, top_k)
        context = "\n".join([d.page_content for d in docs])

        response = self.llm.predict(
            RAG_PROMPT.format(context=context, question=question)
        )

        return {
            "answer": response,
            "num_sources": len(docs),
            "sources": docs if include_sources else None
        }