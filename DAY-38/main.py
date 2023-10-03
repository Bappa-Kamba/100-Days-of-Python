import requests
from datetime import datetime

APP_ID = "95f42386"
API_KEY = "70fff1b0486fcc350a968849e2b868f5"
BASE_ENDPOINT = "https://trackapi.nutritionix.com/v2"
SHEETY_ENDPOINT = "https://api.sheety.co/99fcc7dea1608fb29fc6b763c8c0c6c8/myWorkouts/workouts"

now = datetime.now()

request_body = {
    "query" : input("What exercise(s) did you do today? "),
    "gender" : "male",
    "age" : 23,
    "weight_kg" : 65,
    "height_cm" : 178
}

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}

response = requests.post(
    url=f"{BASE_ENDPOINT}/natural/exercise",
    json=request_body,
    headers=headers
)

workout_list = response.json()['exercises']
workout_data = {
    "workout" : {}
}
workout_header = {
    "Authorization": "Bearer uybyvttcr56765cr56e5cyivkhjnm;,.l,ljmhngbvfcxertgv"
}
for workout in workout_list:
    workout_data["workout"]["date"] = now.strftime("%d/%m/%Y")
    workout_data["workout"]["time"] = now.strftime("%X")
    workout_data["workout"]["exercise"] = workout['name']
    workout_data["workout"]["duration"] = workout['duration_min']
    workout_data["workout"]["calories"] = workout['nf_calories']
    res = requests.post(url=SHEETY_ENDPOINT, json=workout_data, headers=workout_header)
    print(res.text)
