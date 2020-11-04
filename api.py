import requests
import json
response = requests.get("http://api.open-notify.org/iss-now.json")
dictionary = json.dumps(response.json(), sort_keys = True, indent = 4) #convert to a python object
print(dictionary)
json_response = response.json()
#parse out the latitude and longitude from the json_response
#longitude=
#latitude=
#print('Longitude: ', longitude)
#print('Latitude: ', latitude)
