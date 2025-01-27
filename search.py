import cohere

from qdrant_client import QdrantClient


co = cohere.Client(api_key="")

phrases = ["ماهي ايات الحمد"]

model = "embed-multilingual-light-v3.0"
input_type = "search_query"

res = co.embed(
    texts=phrases,
    model=model,
    input_type=input_type,
    embedding_types=["float"],
)
vector = res.embeddings.model_dump()['float_'][0]

client = QdrantClient(url="http://localhost/", port=6333)
collection_name= 'qurani-ai'

result = client.query_points(
                collection_name=collection_name,
                limit=1,
                query=vector
            )
print(result)