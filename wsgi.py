from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.search_router import quran_search

# Initialize FastAPI app
app = FastAPI(title="Quran APIs", version="0.1.0")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include search router
app.include_router(quran_search, prefix="/search", tags=["search"])
