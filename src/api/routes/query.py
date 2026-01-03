"""
Query endpoints
"""
from fastapi import APIRouter, Depends, HTTPException

from src.api.main import get_rag_chain
from src.api.models.requests import QueryRequest
from src.api.models.responses import QueryResponse

router = APIRouter()


@router.post("/", response_model=QueryResponse)
async def query_documents(
    request: QueryRequest,
    rag_chain=Depends(get_rag_chain),
):
    """
    Run a query through the RAG pipeline.
    """
    try:
        result = rag_chain.query(
            question=request.question,
            top_k=request.top_k,
            include_sources=request.include_sources,
            filters=request.filters,
        )
        return QueryResponse(**result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))