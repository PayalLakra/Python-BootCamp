'''
Topics to be Covered:
- API Authentication and its need
- Use of API Keys to Authenticate and get Weather from OpenWeatherMap
- Challenge - Check if it will rain in next 12 Hours
- Sending SMS via the Twilio API
- Use PythonAnywhere to Automate Python Script
- Understanding Environment Variables and Hiding API keys
'''

# Use of API Keys to Authenticate and get Weather from OpenWeatherMap.
import requests

API = "22eb336d761c973b4ee620d5de8053f7"
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

PARAMETERS = {
    "lat": 28.704060, 
    "lon": 77.102493,
    "appid": API
}

response = requests.get(OWN_ENDPOINT, params=PARAMETERS)
print(response.json())

# PythonAnywhere is used to Host, run and code Python in Cloud.
# Environment Variables are used for Convenience and Security.
# Environment variables essentially allow us to separate out where we store our keys, our secret stuff, and various other variables away from where our code base is located.