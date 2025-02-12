from fastapi import FastAPI

from app.api.search_router import quran_search

# Initialize FastAPI app
app = FastAPI(title="Quran APIs", version="0.1.0")

# Include search router
app.include_router(quran_search, prefix="/search", tags=["search"])

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI app
    uvicorn.run(app, host="127.0.0.1", port=8000)
