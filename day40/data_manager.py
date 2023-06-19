import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/96947b6525ffe6426507c482d3588453/myWorkouts/prices"

headers_bearer = {
    "Authorization": "Bearer alex123"
}


class DataManager:

    def __init(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers_bearer)
        data = response.json()
        pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data, headers=headers_bearer)
            print(response.text)
