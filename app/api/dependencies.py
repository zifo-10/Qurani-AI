from app.core.cohere_client import CohereClient
from app.core.config import config
from app.core.mongo_cleint import MongoRepository
from app.core.vector_db import VectorDB
from app.services.search_service import SearchService


def get_qdrant_client():
    return VectorDB(url=config.QDRANT_URI, api_key=config.QDRANT_API_KEY)


def get_cohere_client():
    return CohereClient(api_key=config.COHERE_API_KEY)


def get_mongo_repository():
    return MongoRepository(url=config.MONGO_URI)


def get_search_service():
    return SearchService(qdrant=get_qdrant_client(),
                         cohere=get_cohere_client(),
                         mongo_repo=get_mongo_repository())
