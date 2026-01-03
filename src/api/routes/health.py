"""
Health check endpoints
"""
from datetime import datetime
from fastapi import APIRouter

from config.settings import settings

router = APIRouter()


@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "environment": settings.ENV,
    }