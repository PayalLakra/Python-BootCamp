import requests
from twilio.rest import Client

API = "22eb336d761c973b4ee620d5de8053f7"
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "sid get from twilio login"
auth_token = "get from twilio login"

PARAMETERS = {
    "lat": 28.704060, 
    "lon": 77.102493,
    "appid": API,
    "cnt" : 4
}

response = requests.get(OWN_ENDPOINT, params=PARAMETERS)
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It is going to rain today, Bring Umbrella.",
            from_="+14329042",
            to="8ygi"
    )
    print(message.status)

# Not professional to use account_sid etc. to upload on github or anywhere as it should be personal.
# So best way is-
# api_key = os.environ.get("API_KEY")  [where API_KEY is created in environment variables.]