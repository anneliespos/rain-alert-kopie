import requests
from twilio.rest import Client

MY_LAT = 51.507351
MY_LONG = -0.127758
api_key = "4303269376d8edc3cff3e113700d453f"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "account sid from site"
auth_token = "your auth token from site"

weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain=True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring an umbrella",
        from= "+15123456789",        #new phone number you got from twilio
        to= "+15987654321"
    )      #your own verifier phone number (that you signed up with)

    print(message.status)



