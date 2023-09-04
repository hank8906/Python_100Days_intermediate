import requests
import datetime as dt
import os

exercise = input('Tell me which exercise you did: ')

endpoints = f"https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": os.environ['APP_ID'],
    "x-app-key": os.environ['API_KEY'],
    "Content-Type": "application/json"
}

parameters = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 77,
    "height_cm": 175,
    "age": 23
}

response = requests.post(url=endpoints, headers=headers, json=parameters)
exercises_list = response.json()["exercises"]
# print(response.json()["exercises"])

# ------------------------Making requests in Sheety---------------------------- #

sheety_endpoints = os.environ['sheety_endpoints']
username = os.environ['username']
password = os.environ['password']


for exercise in exercises_list:

    now = dt.datetime.now()
    now_date = now.strftime("%d/%m/%Y")
    now_time = now.strftime("%X")

    parameters = {
       "workout": {
           "date": now_date,
           "time": now_time,
           "exercise": exercise["user_input"].title(),
           "duration": exercise["duration_min"],
           "calories": exercise["nf_calories"]
        }
    }

    exercise_response = requests.post(url=sheety_endpoints, json=parameters, auth=(username, password))

    print(exercise_response.text)

