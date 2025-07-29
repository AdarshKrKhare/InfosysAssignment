from fastapi import FastAPI
from routers import upload, meeting, search, rag

app = FastAPI()

app.include_router(upload.router)
app.include_router(meeting.router)
app.include_router(search.router)
app.include_router(rag.router)