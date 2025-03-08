from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
from backend.app.utils import parse_resume


router = APIRouter()

RESUME_FOLDER = Path("backend/resumes")


@router.post("/upload/")
async def upload_resume(file: UploadFile = File(...)):
    """
    Uploads a resume (PDF/DOCX), stores it, extracts text, and returns parsed content.
    """
    file_ext = file.filename.split(".")[-1].lower()
    if file_ext not in ["pdf", "docx"]:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file format. Only PDF and DOCX allowed.",
        )

    file_path = RESUME_FOLDER / file.filename

    # Save the file
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Parse the resume
    try:
        parsed_text = parse_resume(str(file_path))
        return JSONResponse(
            content={"filename": file.filename, "parsed_text": parsed_text}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing document: {str(e)}")
