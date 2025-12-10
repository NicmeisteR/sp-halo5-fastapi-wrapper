from fastapi import FastAPI
from app.adapters.api import router as api_router

app = FastAPI(title="Halo 5 API Wrapper")

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Halo 5 API Wrapper is running"}

app.include_router(api_router, prefix="/api")
