import requests
from dotenv import load_dotenv
import os 
import json 
import time 


load_dotenv()

COLLEGESCORE_API_KEY =  os.getenv("COLLEGESCORE_API_KEY")

def paginate_through_json(json_object, current_page, total_pages, pages_per_page):
  print('lel')


def get_university_data_http(**params):

    all_data = dict()

    url = f'https://api.data.gov/ed/collegescorecard/v1/schools?api_key={COLLEGESCORE_API_KEY}'

    status = requests.get(url, params=params)
    metadata = status['metadata']
    current_page, total_pages = metadata['page'], metadata['total']

    while current_page<total_pages:

        status = requests.get(url, params=params)

        response = status.content

        response_pretty = json.loads(response)


        if response_pretty:
            try:
                results = response_pretty['results']
            except json.JSONDecodeError as e:
                print("object is empty")    
            else:
                print(results)

        all_data.update(results)
    
        new_metadata = response_pretty['metadata']
        current_page = new_metadata['current_page']
        time.sleep(1)        
    return all_data
