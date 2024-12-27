'''
Topics to be covered:
- API
- API Endpoint and making calls
- Working with responses- HTTP Codes, Exceptions & JSON Data
- Challenge
- Understand API Parameters
- ISS Overhead Notifier Project
'''

# API's are  all are a set of commands, functions, protocols, and objects that programmers can use to create software or interact with an external system.
# API is an interface or rather a sort of barrier between your program and an external system.

# Making a request to ISS location API
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)               # <Response [200]>
print(response.status_code)   # 200
response.raise_for_status()

data = response.json()
# data = response.json()["Any Key"]
print(data)

# 1XX : Hold On
# 2XX : Here you go
# 3XX : Go away
# 4XX : You screwed up
# 5XX : I Screwed Up