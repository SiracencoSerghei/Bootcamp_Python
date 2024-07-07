import os
from pprint import pprint

import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_URL")
class DataManager:
    def __init__(self):
        self._bearer_header = {
"Authorization": f"Bearer {os.environ.get('SHEETY_TOKEN', 'XXXXXXX')}"
}
        self.destination_data = {}
        
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self._bearer_header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
	    for city in self.destination_data:
		    new_data = {
			    "price": {
				    "iataCode": city["iataCode"]
			    }
		    }
		    response = requests.put(
			    url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
			    json=new_data,
			    headers=self._bearer_header
		    )
		    print("update_destination_codes ", response.json())
		    
if __name__ == "__main__":
	data = DataManager()
	data.get_destination_data()
	pprint(data.destination_data)