from cloud.azure_storage import download_csv, upload_csv
from src.data_engineering.clean_data import clean_data
from src.data_engineering.inspect_data import inspect_data


RAW_FILE_PATH = "raw/animal_data.csv"
PROCESSED_FILE_PATH = "processed/cleaned_animal_data.csv"


def azure_cleaning_pipeline():
    df = download_csv(
        RAW_FILE_PATH,
        separator=";",
    )

    print("Data before cleaning:")
    inspect_data(df)

    cleaned_df = clean_data(df)

    print("Data after cleaning:")
    inspect_data(cleaned_df)

    upload_csv(
        cleaned_df,
        PROCESSED_FILE_PATH,
    )

    print(
        f"\nCleaned CSV uploaded to Azure: "
        f"{PROCESSED_FILE_PATH}"
    )


if __name__ == "__main__":
    azure_cleaning_pipeline()