import os
from dotenv import load_dotenv
import requests

load_dotenv()

TOKEN_ENDPOINT = os.environ.get("AMADEUS_TOKEN_URL")
AMADEUS_API_KEY = os.environ.get("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.environ.get("AMADEUS_API_SECRET")


class FlightSearch:
    
    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_API_KEY")
        self._api_secret = os.environ.get("AMADEUS_API_SECRET")
        self._token = self._get_new_token()
    
    def _get_new_token(self):
        if not TOKEN_ENDPOINT:
            raise ValueError("AMADEUS_TOKEN_URL environment variable is not set")
        if not AMADEUS_API_KEY:
            raise ValueError("AMADEUS_API_KEY environment variable is not set")
        if not AMADEUS_API_SECRET:
            raise ValueError("AMADEUS_API_SECRET environment variable is not set")

        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': AMADEUS_API_KEY,
            'client_secret': AMADEUS_API_SECRET
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        # print(response.json())
        return response.json()['access_token']
        
token = FlightSearch()
print(token._token)
