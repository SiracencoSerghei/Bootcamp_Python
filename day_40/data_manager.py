import os
from pprint import pprint

import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_URL")
SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")

class DataManager:
    def __init__(self):
        self._bearer_header = {
            "Authorization": f"Bearer {os.environ.get('SHEETY_TOKEN', 'XXXXXXX')}"
        }
        self.prices_endpoint = SHEETY_PRICES_ENDPOINT
        self.users_endpoint = SHEETY_USERS_ENDPOINT
        self.destination_data = {}
        self.customer_data = {}
    
    def get_destination_data(self):
        response = requests.get(url=self.prices_endpoint, headers=self._bearer_header)
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
    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint, headers=self._bearer_header)
        data = response.json()
        self.customer_data = data["users"]
        pprint(self.customer_data)
        return self.customer_data
    


if __name__ == "__main__":
    data = DataManager()
    data.get_destination_data()
    pprint(data.destination_data)
    data.get_customer_emails()
    pprint(data.customer_data)
    