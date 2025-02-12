from bson import ObjectId
from pymongo import MongoClient

from app.models.aya import QuranModel


class MongoRepository:
    def __init__(self, url: str):
        self.client = MongoClient(url)
        self.db = self.client["Qurani"]
        self.collection = self.db["mokhtaser_tafseer_quran"]

    def get_data(self, ids_list: list) -> list[QuranModel]:
        """"
        Get data from MongoDB based on the provided list of IDs.

        This method fetches data from MongoDB based on the provided list of IDs,
        returning a list of QuranModel instances.

        :param ids_list: The list of IDs to fetch data for.
        :return: The list of QuranModel instances.
        """
        try:
            aya_list = []
            for mongo_id in ids_list:
                document = self.collection.find_one({"_id": ObjectId(mongo_id)})
                aya_list.append(QuranModel(**document))
            return aya_list
        except Exception as e:
            return []