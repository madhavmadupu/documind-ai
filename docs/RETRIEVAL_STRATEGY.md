# Retrieval Strategy

DocuMind AI uses dense vector retrieval as its primary retrieval mechanism.

---

## Dense Retrieval

Technique:
- Cosine / L2 similarity on embeddings

Advantages:
- Semantic understanding
- Robust to paraphrasing
- Language-agnostic

---

## Retrieval Flow

Query
 → Embed query
 → FAISS nearest neighbor search
 → Top-K document chunks

---

## Trade-offs

Pros:
- High recall
- Strong semantic match

Cons:
- Less precise for exact keyword queries
- Requires good chunking

---

## Future Extensions

Planned enhancements:
- Hybrid retrieval (BM25 + dense)
- Cross-encoder reranking
- Metadata-based filtering

---

## Why Recruiters Care

This demonstrates:
- Understanding of IR fundamentals
- Awareness of retrieval failure modes
- Ability to evolve beyond tutorials
