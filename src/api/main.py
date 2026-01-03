"""
FastAPI application entrypoint for DocuMind AI
"""
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.settings import settings
from config.logging_config import setup_logging

from src.api.routes import health, documents, query
from src.generation.rag_chain import RAGChain
from src.ingestion.pipeline import IngestionPipeline

# ------------------------------------------------------------------
# Logging
# ------------------------------------------------------------------
setup_logging()
logger = logging.getLogger(__name__)

# ------------------------------------------------------------------
# Global singletons (initialized at startup)
# ------------------------------------------------------------------
rag_chain: RAGChain | None = None
ingestion_pipeline: IngestionPipeline | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifecycle management.
    Initializes heavy components once.
    """
    global rag_chain, ingestion_pipeline

    logger.info("Starting DocuMind AI API")

    rag_chain = RAGChain()
    ingestion_pipeline = IngestionPipeline()

    yield

    logger.info("Shutting down DocuMind AI API")


app = FastAPI(
    title="DocuMind AI",
    description="Production-grade Retrieval-Augmented Generation system",
    version="1.0.0",
    lifespan=lifespan,
)

# ------------------------------------------------------------------
# Middleware
# ------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------------------------
# Routers
# ------------------------------------------------------------------
app.include_router(health.router, prefix="/api", tags=["health"])
app.include_router(documents.router, prefix="/api/documents", tags=["documents"])
app.include_router(query.router, prefix="/api/query", tags=["query"])


@app.get("/")
async def root():
    return {
        "service": "DocuMind AI",
        "status": "running",
        "environment": settings.ENV,
        "docs": "/docs",
    }


# ------------------------------------------------------------------
# Dependency helpers
# ------------------------------------------------------------------
def get_rag_chain() -> RAGChain:
    if rag_chain is None:
        raise RuntimeError("RAGChain not initialized")
    return rag_chain


def get_ingestion_pipeline() -> IngestionPipeline:
    if ingestion_pipeline is None:
        raise RuntimeError("IngestionPipeline not initialized")
    return ingestion_pipeline