import requests
from datetime import datetime
import os

API_ID = os.environ["NUTRITIONIX_API_ID"]
API_KEY = os.environ["NUTRITIONIX_API_KEY"]
USERNAME = os.environ["SHEETY_USER"]
PASSWORD = os.environ["SHEETY_PASS"]
SHEET_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

QUERY = input("What exercise did you do? ")
GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 180
AGE = 31

parameters = {
    "query": QUERY,
    "gender": GENDER,
    "weight_kg": float(WEIGHT_KG),
    "height_cm": float(HEIGHT_CM),
    "age": AGE
}

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

r = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=headers)
r.raise_for_status()
result = r.json()

today_date = datetime.now().date().strftime("%d/%m/%Y")
current_time = datetime.now().time().strftime("%X")

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": str(today_date),
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

# sheet_r = requests.post(url=SHEET_ENDPOINT, json=sheet_input)

# Basic authentication
sheet_r = requests.post(
    SHEET_ENDPOINT,
    json=sheet_input,
    auth=(
        USERNAME,
        PASSWORD
    )
)
print(sheet_r.text)

