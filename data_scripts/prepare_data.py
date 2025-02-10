import requests
import pandas as pd


class DataPreparation:
    def __init__(self):
        pass

    def download_tafseer_data(self):
        """
        Downloads Tafseer data for all Surahs from the Quranic API and saves it to a CSV file.
        This method fetches Tafseer data for each Surah (from 1 to 114) using the Quranic API,
        concatenates the data into a single DataFrame, and saves it to 'mokhtaser_tafseer.csv'.
        If an error occurs during the download process, the partially downloaded data is still
        saved to 'mokhtaser_tafseer.csv' and the exception is raised.
        Raises:
            Exception: If there is an error during the download process, an exception is raised
                   with a message indicating the error.
        """

        try:
            quranic_api = "https://quranenc.com/api/v1/translation/sura/arabic_mokhtasar/"
            tafseer_df = None
            for sura_index in range(1, 115):
                sura_tafseer = requests.get(url=f"{quranic_api}{sura_index}")
                sura_tafseer_list = sura_tafseer.json()['result']
                sura_tafseer_df = pd.DataFrame(sura_tafseer_list)
                tafseer_df = pd.concat(
                    [tafseer_df, sura_tafseer_df], ignore_index=True)
            tafseer_df.to_csv('mokhtaser_tafseer.csv')
        except Exception as e:
            tafseer_df.to_csv('mokhtaser_tafseer.csv')
            raise Exception(f"Error while download_tafseer_data: {str(e)}")

    def prepare_dataframe(self, tafseer_df_path: str, quran_df_path: str):
        """
        Prepares and merges data from two CSV files containing Tafseer and Quran information.
        Args:
            tafseer_df_path (str): The file path to the Tafseer CSV file.
            quran_df_path (str): The file path to the Quran CSV file.
        Returns:
            pd.DataFrame: A merged DataFrame containing selected columns from both Tafseer and Quran data.
        Raises:
            Exception: If there is an error while reading the CSV files or merging the DataFrames.
        """

        try:
            tafseer_df = pd.read_csv(tafseer_df_path)
            quran_df = pd.read_csv(quran_df_path)

            tafseer_df = tafseer_df.rename(columns={
                                           'translation': 'Tafsser', 'arabic_text': "Ayah", 'aya': 'aya_index', 'sura': 'sura_index'})
            tafseer_df = tafseer_df[['sura_index',
                                     'aya_index', 'Ayah', 'Tafsser']]
            quran_df = quran_df[[
                'number', 'name', 'revelation_place', 'verses_count', 'words_count']]

            merged_df = pd.merge(
                tafseer_df, quran_df, left_on='sura_index', right_on='number', how='inner')
            merged_df.to_csv('data_scripts/mergerd_df.csv')
            return merged_df
        except Exception as e:
            raise Exception(f"Error while prepare_dataframe: {str(e)}")

    def prepare_json_data(self, df: pd.DataFrame):
        """
        Converts a pandas DataFrame to a list of dictionaries.
        Args:
            df (pd.DataFrame): The DataFrame to convert.
        Returns:
            list: A list of dictionaries where each dictionary represents a row in the DataFrame.
        Raises:
            Exception: If an error occurs during the conversion process.
        """

        try:
            rows_list = df.to_dict(orient="records")
            return rows_list
        except Exception as e:
            raise Exception(f"Error while prepare_json_data: {str(e)}")
