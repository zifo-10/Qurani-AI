from qdrant_client import QdrantClient, models


class VectorDB:
    def __init__(self, url: str, api_key: str):
        self.client = QdrantClient(url=url, api_key=api_key)
        self.collection = 'qurani'

    def search(self, vector, limit, score_threshold):
        results = self.client.query_points(
            collection_name=self.collection,
            query=vector,
            limit=limit,
            search_params=models.SearchParams(exact=True),
            score_threshold=score_threshold
        )
        ids_list = []
        points = results.model_dump()['points']
        for point in points:
            mongo_id = point['payload']['mongo_id']
            ids_list.append(mongo_id)
        return list(set(ids_list))
