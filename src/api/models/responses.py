"""
API response schemas
"""
from typing import List, Optional, Dict, Any
from pydantic import BaseModel


class SourceDocument(BaseModel):
    content: str
    metadata: Dict[str, Any]


class QueryResponse(BaseModel):
    answer: str
    num_sources: int
    sources: Optional[List[SourceDocument]] = None


class IngestionResponse(BaseModel):
    success: bool
    file_path: Optional[str] = None
    num_chunks: Optional[int] = None
    processing_time_seconds: Optional[float] = None
    error: Optional[str] = None