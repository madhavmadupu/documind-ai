# Evaluation Framework

Evaluation is a first-class citizen in DocuMind AI.

---

## Why Evaluation Matters

Most RAG demos fail because:
- No hallucination measurement
- No retrieval quality analysis
- No reproducibility

This project explicitly addresses that.

---

## Metrics Used (RAGAS)

1. Faithfulness
   - Measures hallucinations
   - Checks if answer is supported by context

2. Answer Relevance
   - Measures relevance to the question

---

## Evaluation Flow

1. Prepare Q&A dataset
2. Run RAG pipeline
3. Compare answers vs context
4. Generate metric scores

---

## Output

- Quantitative scores
- Model comparison
- Retrieval strategy comparison

---

## Interview-Ready Insight

“I didn’t trust the model blindly — I measured hallucinations and relevance using RAGAS and used that data to guide improvements.”
