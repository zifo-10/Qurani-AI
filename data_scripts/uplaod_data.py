import json
from typing import List
from uuid import uuid4
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
import cohere
import pandas as pd
from pymongo import MongoClient
from bson.objectid import ObjectId
from models import MongoSchema


class DataUploader:
    """
    DataUploader is a class responsible for uploading data to MongoDB and Qdrant, 
    embedding text data using Cohere, and managing collections in Qdrant.
    """

    def __init__(self, qdrant_url: str,
                 qdrant_api_key: str,
                 cohere_api_key: str,
                 mongo_uri: str):
        self.qdrant_client = QdrantClient(url=qdrant_url,
                                          api_key=qdrant_api_key)
        self.cohere_client = cohere.Client(api_key=cohere_api_key)
        self.mongo_client = MongoClient(mongo_uri)

    def embed_data(self, model: str, tafseer_text_list: List[str], input_type: str):
        """
        Embeds a list of tafseer texts using the specified model and input type.
        Args:
            model (str): The name of the model to use for embedding.
            tafseer_text_list (List[str]): A list of tafseer texts to be embedded.
            input_type (str): The type of input to be used for embedding.
        Returns:
            List: A list of embeddings for the provided tafseer texts.
        Raises:
            Exception: If an error occurs during the embedding process.
        """

        try:
            return self.cohere_client.embed(texts=tafseer_text_list, model=model, input_type=input_type).embeddings
        except Exception as e:
            raise Exception(f"Error while embed_data: {str(e)}")

    def insert_data_into_qdrant(self, points, collection_name: str, vector_length: int):
        """
        Inserts data points into a specified Qdrant collection. If the collection does not exist, it will be created.
        Args:
            points (list): A list of data points to be inserted into the collection.
            collection_name (str): The name of the collection where the data points will be inserted.
            vector_length (int): The length of the vectors to be stored in the collection.
        Raises:
            Exception: If there is an error during the insertion process, an exception is raised with an error message.
        """

        try:
            # Create collection if not exist
            if collection_name not in [c.name for c in self.qdrant_client.get_collections().collections]:
                self.qdrant_client.create_collection(
                    collection_name=collection_name,
                    vectors_config=VectorParams(
                        size=vector_length, distance=Distance.COSINE)
                )
            self.qdrant_client.upsert(
                collection_name=collection_name, points=points)
        except Exception as e:
            raise Exception(f"Error while insert_data_into_qdrant: {str(e)}")

    def upload_data(self,
                    mongo_db_name: str,
                    mongo_collection_name: str,
                    tafseer_df: list[dict],
                    qdrant_collection_name: str,
                    model: str = 'embed-multilingual-light-v3.0',
                    vector_length: int = 384):
        """
        Uploads data to MongoDB and Qdrant.
        Args:
            mongo_db_name (str): The name of the MongoDB database.
            mongo_collection_name (str): The name of the MongoDB collection.
            tafseer_df (list[dict]): A list of dictionaries containing the data to be uploaded.
            qdrant_collection_name (str): The name of the Qdrant collection.
            model (str, optional): The model to be used for embedding the data. Defaults to 'embed-multilingual-light-v3.0'.
            vector_length (int, optional): The length of the vectors to be used in Qdrant. Defaults to 384.
        Returns:
            str: A success message if the data is inserted successfully.
        Raises:
            Exception: If there is an error during the upload process.
        """
        try:
            # Insert data into Mongo
            mongo_ids = self.insert_data_into_mongo(
                db_name=mongo_db_name, collection_name=mongo_collection_name, data_list=tafseer_df)

            # Embed data
            tafseer_list = [item['Tafsser'] for item in tafseer_df]
            tafseer_embedding_list = self.embed_data(
                model=model, tafseer_text_list=tafseer_list, input_type='search_document')
            
            # Construct point
            points = self.construct_points(vectors=tafseer_embedding_list,
                                           mongo_ids=mongo_ids,
                                           mongo_collection_name=mongo_collection_name)
            self.insert_data_into_qdrant(
                points=points, collection_name=qdrant_collection_name, vector_length=vector_length)
            return 'Data inserted successfully'
        except Exception as e:
            raise Exception(f"Error while upload_data: {str(e)}")

    def insert_data_into_mongo(self, db_name: str, collection_name: str, data_list: list[dict]):
        """
        Inserts a list of dictionaries into a specified MongoDB collection.
        Args:
            db_name (str): The name of the database.
            collection_name (str): The name of the collection.
            data_list (list[dict]): A list of dictionaries containing the data to be inserted. 
            Each dictionary should have the keys 'Ayah', 'Tafsser', 'sura_index', 'aya_index', 'name', and 'revelation_place'.
        Returns:
            list: A list of ObjectIds of the inserted documents.
        Raises:
            Exception: If there is an error during the insertion process.
        """
        try:
            db = self.mongo_client[db_name]
            collection = db[collection_name]

            # Insert data into MongoDB
            validated_data = [MongoSchema(ayah=data_list[i]['Ayah'],
                                          tasfeer=data_list[i]['Tafsser'],
                                          sura_index=data_list[i]['sura_index'],
                                          aya_index=data_list[i]['aya_index'],
                                          sura_name=json.loads(
                                              data_list[i]['name']),
                                          sura_type=json.loads(
                                              data_list[i]['revelation_place']),
                                          chunks=[data_list[i]['Ayah']],
                                          tasfeer_name="Mokhtaser tafseer"
                                          ) for i in range(len(data_list))]
            insert_data = [item.model_dump() for item in validated_data]
            result = collection.insert_many(insert_data)
            return result.inserted_ids
        except Exception as e:
            raise Exception(f"Error while insert_data_into_mongo: {str(e)}")
        finally:
            # Close connection
            self.mongo_client.close()

    def construct_points(self,
                         vectors: List[List[float]],
                         mongo_ids: List[ObjectId],
                         mongo_collection_name: str):
        """
        Constructs a list of PointStruct objects from given vectors and MongoDB IDs.
        Args:
            vectors (List[List[float]]): A list of vectors, where each vector is a list of floats.
            mongo_ids (List[ObjectId]): A list of MongoDB ObjectIds corresponding to the vectors.
            mongo_collection_name (str): The name of the MongoDB collection.
        Returns:
            List[PointStruct]: A list of PointStruct objects with the given vectors and MongoDB IDs.
        Raises:
            Exception: If the lengths of vectors and mongo_ids do not match or any other error occurs during construction.
        """
        try:
            if len(vectors) != len(mongo_ids):
                raise Exception("List are of same length, there is missing data"
                                f"{len(vectors)} != {len(mongo_ids)}")
            points = [PointStruct(id=str(uuid4()),
                                  vector=vectors[i],
                                  payload={"mongo_id": str(mongo_ids[i]),
                                           "mongo_collection": mongo_collection_name}
                                  ) for i in range(len(vectors))]
            return points
        except Exception as e:
            raise Exception(f"Error while construct_points: {str(e)}")
