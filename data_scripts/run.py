from prepare_data import DataPreparation
from uplaod_data import DataUploader
from dotenv import load_dotenv
import os


# load .end file
load_dotenv()

# downloading data
# DataPreparation().download_tafseer_data()

# Prepare data
all_df = DataPreparation().prepare_dataframe(tafseer_df_path=os.getenv('TAFSEER_DF_PATH'),
                                             quran_df_path=os.getenv('QURAN_DF_PATH'))

data_list = DataPreparation().prepare_json_data(df=all_df)

# Upload data
data_uploder = DataUploader(qdrant_url=os.getenv('QDRANT_URL'),
                            qdrant_api_key=os.getenv('QDRANT_API_KEY'),
                            mongo_uri=os.getenv('MONGO_URL'),
                            cohere_api_key=os.getenv('COHERE_API_KEY'))

# Test with 5 rows
inserted_data = data_uploder.upload_data(mongo_db_name=os.getenv('MONGO_DB_NAME'),
                                         mongo_collection_name=os.getenv(
                                             'MONGO_COLLECTION_NAME'),
                                         qdrant_collection_name=os.getenv(
                                             'QDRANT_COLLECTION_NAME'),
                                         tafseer_df=data_list[0:5])

print(inserted_data)
