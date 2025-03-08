# Entry point (FastAPI/Flask server)
from fastapi import FastAPI
from backend.app.routes.parsing import router as parsing_router

app = FastAPI()

app.include_router(parsing_router, prefix="/parsing", tags=["Parsing"])
