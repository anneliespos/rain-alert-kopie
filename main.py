import requests
from twilio.rest import Client

MY_LAT = 51.507351      #example in London
MY_LONG = -0.127758     #example in London
api_key = "your api key"
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
        from= "twilio phone number",        #new phone number you got from twilio
        to= "your own phone number"
    )      #your own verifier phone number (that you signed up with)

    print(message.status)



