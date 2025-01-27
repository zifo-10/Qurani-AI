from pymongo import MongoClient

# Connect to the local MongoDB instance
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['Qurani']
collection = db['qurani']
documents = collection.find()

# Print documents
for document in documents:
    mongo_id = str(document['_id'])
    surah_name_ar = document['surah_name_ar']
    print(f"MongoDB document ID: {mongo_id}, Surah name: {surah_name_ar}")
