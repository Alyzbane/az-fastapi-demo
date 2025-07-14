from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.setup_model import download_model
from src.api.v1.endpoints import router as api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Ready the model and tokenizer download cached during Docker build
    tokenizer, model = download_model("cardiffnlp/twitter-roberta-base-sentiment")

    # Set the model, tokenizer, and labels in the app context
    app.tokenizer = tokenizer
    app.model = model
    app.labels = ["negative", "neutral", "positive"]

    yield

    # Clean up the ML models and release the resources
    del app.model
    del app.tokenizer
    del app.labels


app = FastAPI(lifespan=lifespan)


app.include_router(api_router, prefix="/v1", tags=["Public API"])

@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {"status": "ok", "message": "API is running"}