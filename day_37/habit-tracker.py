from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = os.getenv("PIXELA_USERNAME").lower()
AGREE = os.getenv("agreeTermsOfService")
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
	"token": TOKEN,
	"username": USERNAME,
	"agreeTermsOfService": AGREE,
	"notMinor": "yes",
}
# use the code (commented below) only once to create a new user!

# print(user_params)
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.json())

# created https://pixe.la/@sergiosiracenco

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
	"id": GRAPH_ID,
	"name": "Cycling graph",
	"unit": "Km",
	"type": "float",
	"color": "ajisai",
}
headers = {
	"X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.json())
# created at https://pixe.la/v1/users/sergiosiracenco/graphs/graph1.html


# 4 Post value to the graph Call /v1/users/<username>/graphs/<graphID> by HTTP POST.

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# today = datetime(year = 2024, month = 7, day = 4).strftime("%Y%m%d")
print(today)

pixel_data = {
	"date": today.strftime("%Y%m%d"),
	"quantity" : input("How many kilometers did you cycle today?"),
	}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.json())

new_pixel_data = {
	"quantity": "4.5"
}
for_date = today.strftime('%Y%m%d')
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{for_date}"

# response = requests.put(url=update_endpoint, json=new_pixel_data,headers=headers)
# print(response.json())

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{for_date}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.json())