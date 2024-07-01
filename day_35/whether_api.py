import os

import requests
from dotenv import load_dotenv

load_dotenv()

lat = os.getenv("LAT")
lon = os.getenv("LON")
API_KEY = os.getenv("WHETHER_API_KEY")


URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

result = requests.get(URL).json()
print(result)
