from fastapi import APIRouter, Query
from services.chroma_service import retrieve_relevant_chunks
from services.ollama_service import generate_response

router = APIRouter()

@router.get("/api/ask")
async def ask_question(q: str = Query(...)):
    chunks = retrieve_relevant_chunks(q)
    response = generate_response(q, context=chunks)
    return {"answer": response}