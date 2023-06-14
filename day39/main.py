import requests
from datetime import datetime

query = input("What Exercise did you do today? ")

Application_ID = "a628775d"
API_KEY = "27f27ad8d0289c0fe0a9a419c6a42f54"
END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/96947b6525ffe6426507c482d3588453/myWorkouts/workouts"

GENDER = "male"
WEIGHT_KG = 120
HEIGHT_CM = 6.9
AGE = 39

headers = {
    "x-app-id": Application_ID,
    "x-app-key": API_KEY
}

PARAMS = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=END_POINT, json=PARAMS, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    ### with no authentication
    # sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs)

    ## with basic authentication
    # sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, auth=("", ""))

    ##Barier athentication
    bearer_headers = {
        "Authorization": "Bearer "
    }

    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response)

