"""
API request schemas
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    question: str = Field(..., description="User question")
    top_k: int = Field(5, ge=1, le=20)
    include_sources: bool = True
    filters: Optional[Dict[str, Any]] = None

    class Config:
        json_schema_extra = {
            "example": {
                "question": "What is Retrieval-Augmented Generation?",
                "top_k": 5,
                "include_sources": True,
            }
        }