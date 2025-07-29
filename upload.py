from fastapi import APIRouter, UploadFile
from utils.file_utils import save_file
from services.whisper_service import transcribe_audio

router = APIRouter()

@router.post("/api/upload")
async def upload_file(file: UploadFile):
    file_path = save_file(file)
    transcript = transcribe_audio(file_path)
    return {"transcript": transcript}
