
from qdrant_client import QdrantClient
from qdrant_client import models

client = QdrantClient(url="http://localhost/", port=6333)
collection_name= 'qurani-ai'

result = client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE))