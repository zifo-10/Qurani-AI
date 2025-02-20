from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from app.core.e5_client import E5Client  

# Initialize the embedding model once
embedding_model = E5Client()  


# Load environment variables from .env file
load_dotenv()

class Config(BaseSettings):
    QDRANT_URI: str
    QDRANT_API_KEY: str
    MONGO_URI: str
    COHERE_API_KEY: str

    class Config:
        env_file = ".env"

config = Config()