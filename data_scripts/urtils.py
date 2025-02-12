import requests
import pandas as pd


def download_tafseer_data():
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

def prepare_json_data( df: pd.DataFrame):
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
