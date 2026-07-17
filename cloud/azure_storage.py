import os
from io import BytesIO

import pandas as pd
from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_NAME = os.getenv("azure_storage_account")
FILE_SYSTEM_NAME = os.getenv("azure_file_system")

def get_datalake_service_client():
    if not ACCOUNT_NAME:
        raise ValueError("Azure storage account name is not set in environment variables.")
    if not FILE_SYSTEM_NAME:
        raise ValueError("Azure file system name is not set in environment variables.")
    
    credential = DefaultAzureCredential()
    service_client = DataLakeServiceClient(
        account_url=f"https://{ACCOUNT_NAME}.dfs.core.windows.net",
        credential=credential
    )

    return service_client.get_file_system_client(FILE_SYSTEM_NAME)

def download_csv(
        filepath: str,
        separator: str = ";"
)-> pd.DatraFrame:
    file_system_client = get_datalake_service_client()
    file_client = file_system_client.get_file_client(filepath)
    file_bytes = file_client.download_file().readall()
    return pd.read_csv(BytesIO(file_bytes), sep=separator)

def upload_csv(
        dataframe: pd.DataFrame,
        filepath: str,
) -> None:
    file_system_client = get_datalake_service_client()
    file_client = file_system_client.get_file_client(filepath)
    csv_bytes = dataframe.to_csv(index=False).encode("utf-8")
    file_client.upload_data(csv_bytes, overwrite=True)
