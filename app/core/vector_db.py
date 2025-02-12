from qdrant_client import QdrantClient


class VectorDB:
    def __init__(self, url: str, api_key: str):
        self.client = QdrantClient(url=url, api_key=api_key)
        self.collection = 'qurani'

    def search(self, vector, limit):
        results = self.client.query_points(
            collection_name=self.collection,
            limit=limit,
            query=vector
        )
        ids_list = []
        points = results.model_dump()['points']
        for point in points:
            mongo_id = point['payload']['mongo_id']
            ids_list.append(mongo_id)
        return ids_list
