import requests
from dotenv import load_dotenv
import os 

load_dotenv()

COLLEGESCORE_API_KEY =  os.getenv("COLLEGESCORE_API_KEY")

url = f'https://api.data.gov/ed/collegescorecard/v1/schools?api_key={COLLEGESCORE_API_KEY}'



status = requests.get()

print(status) 
