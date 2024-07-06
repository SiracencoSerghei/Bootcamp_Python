import datetime
import requests
import os
import dotenv

dotenv.load_dotenv()

GENDER = os.getenv("GENDER")
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT_CM = os.getenv("HEIGHT_CM")
AGE = os.getenv("AGE")

APP_ID = os.getenv("NUTRITION_ID")
API_KEY = os.getenv("NUTRITION_API_KEY")
USERNAME = os.getenv("USER_NAME")
PASSWD = os.getenv("PASSWD")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

# part 2

sheety_url = 'https://api.sheety.co/0ee5aba96e41c5024cf38dd619181c5e/workoutTracking/workouts'

today_date = datetime.datetime.now().strftime("%d%m%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in result['exercises']:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
#
# auth = (
#     USERNAME,
#     PASSWD
# )
# sheet_response = requests.post(url=sheety_url, json=sheet_inputs, auth=auth)
# print(sheet_response.text)


bearer_header = {
"Authorization": f"Bearer {os.environ.get('SHEETY_TOKEN', 'XXXXXXX')}"
}
sheet_response = requests.post(url=sheety_url, json=sheet_inputs, headers=bearer_header)
print(sheet_response.text)

# for key, value in os.environ.items():
#     print('{}: {}'.format(key, value))