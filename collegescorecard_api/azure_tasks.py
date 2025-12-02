from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
import os 
from dotenv import load_dotenv 
from collegescorecard_api.api import get_university_data_http 
from utils.str_utils import make_string_from_list

load_dotenv()
BLOB_SAS_TOKEN = os.getenv("BLOB_SAS_TOKEN")
BLOB_SAS_URL = os.getenv("BLOB_SAS_URL")
BLOB_ACCOUNT_URL = os.getenv("BLOB_ACCOUNT_URL")

# Acquire a credential object
token_credential = DefaultAzureCredential()

blob_service_client = BlobServiceClient(
        account_url=BLOB_ACCOUNT_URL,
        credential=token_credential)


blob_client = blob_service_client.get_blob_client(container='destination',blob='university_data.txt')


fields= ['id', 'school.name', 'school.state', 'latest.student.size', 
        'latest.cost.tuition.in_state', 'latest.cost.tuition.out_of_state']

str_obj = make_string_from_list(list=fields)

http_params = {'school.name': 'Harvard University','fields': str_obj}

data = get_university_data_http(http_params=http_params)

blob_client.upload_blob(data)
