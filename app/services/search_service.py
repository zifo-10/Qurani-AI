from app.core.cohere_client import CohereClient
from app.core.mongo_cleint import MongoRepository
from app.core.vector_db import VectorDB


class SearchService:
    def __init__(self, qdrant: VectorDB, cohere: CohereClient, mongo_repo: MongoRepository):
        self.qdrant = qdrant
        self.cohere = cohere
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
            embedding = self.cohere.embed_text(texts=[query],
                                               model="embed-multilingual-light-v3.0",
                                               input_type="search_query",
                                               embedding_types=["float"])
            # Step 2: Search in Qdrant
            search_results = self.qdrant.search(vector=embedding,
                                                limit=5)
            # Step 3: Fetch additional data from MongoDB
            enriched_results = self.mongo_repo.get_data(search_results)

            return {"results": enriched_results}
        except Exception as e:
            raise ValueError(f"Failed to search: {e}")
