# DocuMind AI – Production RAG System

DocuMind AI is a production-grade Retrieval-Augmented Generation system
designed to process enterprise documents and provide grounded,
citation-backed answers.

## Features
- Multi-format document ingestion
- Vector search with FAISS
- Hybrid retrieval architecture
- OpenAI-powered generation
- RAGAS-based evaluation
- FastAPI backend
- Dockerized deployment

## Project Structure

```plaintext
documind-ai/
│
├── requirements.txt
├── .env.example
├── Dockerfile
├── docker-compose.yml
│
├── config/
│   ├── settings.py
│   └── logging_config.py
│
├── src/
│   ├── ingestion/
│   │   ├── loaders.py
│   │   ├── chunking.py
│   │   ├── preprocessors.py
│   │   └── pipeline.py
│   │
│   ├── embeddings/
│   │   └── embedding_manager.py
│   │
│   ├── retrieval/
│   │   ├── vector_store.py
│   │   └── hybrid_retriever.py
│   │
│   ├── generation/
│   │   ├── llm_manager.py
│   │   ├── prompts.py
│   │   └── rag_chain.py
│   │
│   ├── evaluation/
│   │   ├── metrics.py
│   │   └── evaluator.py
│   │
│   ├── api/
│   │   ├── main.py
│   │   ├── routes/
│   │   │   ├── health.py
│   │   │   ├── documents.py
│   │   │   └── query.py
│   │   └── models/
│   │       ├── requests.py
│   │       └── responses.py
│
└── README.md
```



## Tech Stack
Python · FastAPI · LangChain · FAISS · OpenAI · RAGAS · Docker

## Run
```bash
docker-compose up --build
