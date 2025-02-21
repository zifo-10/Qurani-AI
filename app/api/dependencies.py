from app.core.cohere_client import CohereClient
from app.core.config import config
from app.core.mongo_cleint import MongoRepository
from app.core.vector_db import VectorDB
from app.services.search_service import SearchService
from app.core.config import embedding_model


def get_qdrant_client():
    return VectorDB(url=config.QDRANT_URI, api_key=config.QDRANT_API_KEY)


def get_embedding_client():
    return embedding_model


def get_mongo_repository():
    return MongoRepository(url=config.MONGO_URI)


def get_search_service():
    return SearchService(qdrant=get_qdrant_client(),
                         embedding_client=get_embedding_client(),
                         mongo_repo=get_mongo_repository())
