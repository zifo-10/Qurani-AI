from app.core.cohere_client import CohereClient
from app.core.embedding_interface import EmbeddingClient
from app.core.mongo_cleint import MongoRepository
from app.core.vector_db import VectorDB


class SearchService:
    def __init__(self, qdrant: VectorDB, embedding_client: EmbeddingClient, mongo_repo: MongoRepository):
        self.qdrant = qdrant
        self.embedding_client = embedding_client
        self.mongo_repo = mongo_repo

    def search(self, query: str) -> dict:
        """
        Search for a given query using the search service.

        This method performs a search operation on the provided query string
        and returns relevant results.

        :param query: The search term to look up.
        :return: The search results.
        """
        try:
            # Step 1: Embed query
            embedding = self.embedding_client.embed_text(texts=[f"query: {query}"])
            # Step 2: Search in Qdrant
            search_results = self.qdrant.search(vector=embedding,
                                                limit=5,
                                                score_threshold=0.84)
            # Step 3: Fetch additional data from MongoDB
            enriched_results = self.mongo_repo.get_data(search_results)

            return {"results": enriched_results}
        except Exception as e:
            raise ValueError(f"Failed to search: {e}")
