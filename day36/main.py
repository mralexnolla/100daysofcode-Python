import requests
import os
from twilio.rest import Client

Endpoint = "https://pro.openweathermap.org/data/2.5/forecast/hourly"
api_key = os.environ.get("OWM_API_KEY")

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

will_rain = False

response = requests.get(Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Hey, It might rain today. Remember to bring an umbrella  ☔️",
        from_='+13614597365',
        to='+233263976829'
    )
    print(message.status)


