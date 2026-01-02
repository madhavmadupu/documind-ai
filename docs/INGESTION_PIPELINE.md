# Document Ingestion Pipeline

The ingestion pipeline transforms unstructured documents into a searchable vector index.

---

## Supported Formats
- PDF
- TXT
- Markdown (extendable)
- Word / Excel (future)

---

## Pipeline Steps

### 1. Document Loading
Uses LangChain document loaders to extract raw text and metadata.

Example:
- PDF → pages
- Text → full content

---

### 2. Preprocessing
Cleaning operations:
- Remove excessive whitespace
- Normalize line breaks
- Preserve semantic structure

Purpose:
- Improve chunk coherence
- Reduce embedding noise

---

### 3. Chunking Strategy

Chunk Size: 500 characters  
Overlap: 100 characters

Why?
- Preserves semantic continuity
- Fits within LLM context windows
- Improves retrieval recall

---

### 4. Embedding Generation
Embeddings generated using:
- Sentence-Transformers (MiniLM)

Reasons:
- Fast
- Open-source
- Strong semantic performance

---

### 5. Vector Storage
Stored in FAISS index:
- Low latency
- In-memory
- Easy to deploy locally or in cloud

---

## Failure Handling
- File-level isolation
- Partial ingestion allowed
- Clear error propagation

---

## Output Metrics
- Number of chunks
- Processing time
- Ingestion success status
