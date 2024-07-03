import json
import os

import requests
from dotenv import load_dotenv

from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

load_dotenv()

lat = os.getenv("LAT")
lon = os.getenv("LON")
API_KEY = os.getenv("WHETHER_API_KEY")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
account_sid = os.getenv("account_sid")
from_number = os.getenv("from_number")
my_tel_number = os.getenv("my_tel_number")


#
# URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
#
# result = requests.get(URL).json()
# print(result)

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
wether_params = {
	"lat": lat,
	"lon": lon,
	"appid": API_KEY,
	"cnt": 4,
	"units": "metric",
}
response = requests.get(OWM_ENDPOINT, wether_params)
response.raise_for_status()
weather_data = response.json()
formatted_data = json.dumps(weather_data, indent=4)
# print(formatted_data)
print(weather_data["list"][0]["weather"][0])
will_rain = False
for hour_data in weather_data["list"]:
	condition_code = hour_data["weather"][0]["id"]
	# print(condition_code)
	if int(condition_code) < 700:
		# print("Bring an umbrella")
		will_rain = True
# proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
if will_rain:
	client = Client(account_sid, TWILIO_TOKEN)
	message = client.messages.create(
		body=f"Hello Sergio, It's going to rain today. Remember to bring an umbrella.",
		from_=from_number,
		to=my_tel_number,
	)
print(message.body)

	