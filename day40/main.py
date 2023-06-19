# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]['iataCode'] == "":
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

# -------------

# import requests
# from pprint import pprint
#
# ### sheety API call
# SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/96947b6525ffe6426507c482d3588453/myWorkouts/prices"
#
# headers_bearer = {
#     "Authorization": "Bearer alex123"
# }
#
# #### Tequila api call
# TEQUILA_API_KEY = "ZXhXFgymD7RgbdcwkADOtkS71UVn1opy"
# TEQUILA_END_POINT = "https://api.tequila.kiwi.com/locations/query"
#
# query = {
#     "term": "LON",
#     "location_types": "city"
# }
#
#
# ###getting sheety data
# def get_destination_data():
#     sheetyresponse = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers_bearer)
#     sheetresult = sheetyresponse.json()['prices']
#     return sheetresult
#
#
# # pprint(get_destination_data()[0]['iataCode'])
#
#
# #### getting the location code
# def get_destination_code(city_name):
#     location_endpoint = TEQUILA_END_POINT
#     headers = {"apikey": TEQUILA_API_KEY}
#     query = {"term": city_name, "location_types": "city"}
#     tequilaResponse = requests.get(url=location_endpoint, headers=headers, params=query)
#     tequilaResult = tequilaResponse.json()['locations'][0]['code']
#     return tequilaResult
#
#
# # pprint(get_destination_code("Paris"))
#
# if get_destination_data()[0]['iataCode'] == "":
#     for row in get_destination_data():
#         row['iataCode'] = get_destination_code(row['city'])
#         new_data = {
#             'price': {
#                 'iataCode': row['iataCode']
#             }
#         }
#         sheetyResponse = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{row['id']}", json=new_data, headers=headers_bearer)
#         pprint(sheetyResponse.text)