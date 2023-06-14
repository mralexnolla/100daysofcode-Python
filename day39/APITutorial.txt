import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER_NAME = "alexese"
TOKEN = "AIjyrNATdsgyAOMHY"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPHID = "walking13"

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"
graph_params = {
    "id": GRAPHID,
    "name": "walking graph",
    "unit": "Km",
    "type": "int",
    "color": "shibafu"

}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.text)

#### Creating the data
today = datetime(year=2023, month=6, day=11)

GRAPH_DETAILS_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPHID}"
# detail_params = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": input(f"How many kilometers did you walk today {today}? ")
# }
#
# response = requests.post(url=GRAPH_DETAILS_ENDPOINT, json=detail_params, headers=headers)
# print(response.text)

#### updating the data
update_today = today.strftime("%Y%m%d")

UPDATE_ENDPOINT = f"{GRAPH_DETAILS_ENDPOINT}/{update_today}"
# update_params = {
#     "quantity": input(f"Update the distance for {today}? ")
# }
#
# response = requests.put(url=UPDATE_ENDPOINT, json=update_params, headers=headers)
# print(response.text)

#delete a habit
response = requests.delete(url=UPDATE_ENDPOINT, headers=headers)
print(response.text)

