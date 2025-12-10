
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.adapters.api import router as api_router

app = FastAPI(
    title="Halo 5 API Wrapper",
    description="A FastAPI wrapper for the Halo 5 API using Hexagonal Architecture. Provides endpoints for player profiles, arena statistics, match history, and ML-based performance predictions.",
    version="1.0.0",
    contact={
        "name": "Schuberg Philis",
        "url": "https://github.com/schuberg-philis",
    },
    license_info={
        "name": "MIT",
    },
    openapi_tags=[
        {"name": "Profile", "description": "Player profile operations"},
        {"name": "Arena", "description": "Arena service record operations"},
        {"name": "Matches", "description": "Match history operations"},
        {"name": "Predictions", "description": "ML-based performance predictions"},
    ]
)

# Allow CORS for Angular frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Halo 5 API Wrapper is running"}

app.include_router(api_router, prefix="/api")
