"""
Document ingestion endpoints
"""
import tempfile
from pathlib import Path

from fastapi import APIRouter, UploadFile, File, Depends, HTTPException

from src.api.main import get_ingestion_pipeline
from src.api.models.responses import IngestionResponse

router = APIRouter()


@router.post("/upload", response_model=IngestionResponse)
async def upload_document(
    file: UploadFile = File(...),
    pipeline=Depends(get_ingestion_pipeline),
):
    """
    Upload and ingest a single document.
    """
    try:
        with tempfile.NamedTemporaryFile(
            delete=False, suffix=Path(file.filename).suffix
        ) as tmp:
            content = await file.read()
            tmp.write(content)
            tmp_path = tmp.name

        result = pipeline.ingest_file(
            tmp_path,
            metadata={"filename": file.filename},
        )

        Path(tmp_path).unlink(missing_ok=True)

        return IngestionResponse(**result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))