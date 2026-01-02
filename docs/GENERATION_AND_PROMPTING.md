# Generation & Prompting Strategy

The generation layer is responsible for producing grounded, faithful answers.

---

## Prompt Design

Key Principles:
- Context-first prompting
- Explicit grounding instruction
- Deterministic generation

Template:
- Context
- Question
- Answer

---

## LLM Configuration

Temperature: 0  
Reason:
- Reduce hallucinations
- Improve repeatability

---

## Context Assembly

- Concatenates retrieved chunks
- Maintains ordering
- Avoids unnecessary verbosity

---

## Hallucination Control

Strategies:
- Retrieval-first answering
- Faithfulness evaluation
- Context-only answering instruction

---

## Source Attribution

Each answer can optionally include:
- Number of sources
- Source content
- Metadata

This is critical for:
- Trust
- Explainability
- Enterprise usage
