# API Documentation

Base URL: `/api`

---

## Health Check

GET `/health`

Returns system status.

---

## Upload Document

POST `/documents/upload`

Form-Data:
- file: document

Response:
- ingestion status
- number of chunks
- processing time

---

## Query

POST `/query`

Body:
```json
{
  "question": "What is RAG?",
  "top_k": 5
}
