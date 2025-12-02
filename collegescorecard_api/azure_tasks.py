from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
import os 
from dotenv import load_dotenv 

load_dotenv()
BLOB_SAS_TOKEN = os.getenv("BLOB_SAS_TOKEN")
BLOB_SAS_URL = os.getenv("BLOB_SAS_URL")

# Acquire a credential object
token_credential = DefaultAzureCredential()

blob_service_client = BlobServiceClient(
        account_url="https://<my_account_name>.blob.core.windows.net",
        credential=token_credential)
