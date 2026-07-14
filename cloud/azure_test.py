import os
from io import BytesIO



import pandas as pd
from azure.identity import AzureCliCredential
from azure.storage.filedatalake import DataLakeServiceClient
from dotenv import load_dotenv

load_dotenv()


ACCOUNT_NAME = os.getenv("azure_storage_account")
FILE_SYSTEM_NAME = os.getenv("azure_file_system")
FILE_PATH = "raw/animal_data.csv"

credential = AzureCliCredential()

service_client = DataLakeServiceClient(
    account_url=f"https://{ACCOUNT_NAME}.dfs.core.windows.net",
    credential=credential,
)

file_system_client = service_client.get_file_system_client(
    FILE_SYSTEM_NAME
)

file_client = file_system_client.get_file_client(FILE_PATH)

download = file_client.download_file()
file_bytes = download.readall()

df = pd.read_csv(BytesIO(file_bytes), sep=";")

print("CSV loaded from Azure.")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print()
print(df.head())