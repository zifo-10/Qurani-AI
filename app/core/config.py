import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

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