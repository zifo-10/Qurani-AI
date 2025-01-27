import cohere
import uuid

from qdrant_client import QdrantClient
from qdrant_client import models

co = cohere.Client(api_key="wyV8xL20jbNxLWhp4aWgtPtfHywPluqhYpDi0cpe")

# get the embeddings
phrases = ["الذين يؤمنون بالغيب ويقيمون الصلاة ومما رزقناهم ينفقون"]

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
payload =  {
    "mongo_id": "67974cb35e8e7e6047695edd",
    "surah_name_ar": "البقرة"
}
result = client.upsert(
            collection_name="qurani-ai",
    points=[models.PointStruct(
        id=str(uuid.uuid4()),
        payload=payload,
        vector=vector)
    ]
        )
