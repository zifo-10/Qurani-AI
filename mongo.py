from bson import ObjectId
from pymongo import MongoClient

# Connect to the local MongoDB instance
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['Qurani']
collection = db['qurani']
documents = collection.find()



def get_document_by_id(ids_list: list):
    """
    Get a document from MongoDB by its ID.
    """
    documents = []
    for mongo_id in ids_list:
        document = collection.find_one({"_id": ObjectId(mongo_id)})
        if document:
            documents.append(document)
    return documents
