import requests
import json


lat = 59.329
lon = 18.069

# Open Weather configuration
API_key = "4c0855da321c0d905dc62f6e3a6c8cff"
ow_endpoint = f"https://api.openweathermap.org/data/3.0/onecall"
ow_param = {
    "lat": lat,
    "lon": lon,
    "appid": API_key
}

# yr configuration
yr_endpoint = "https://api.met.no/weatherapi/locationforecast/2.0/complete"
yr_param = {
    "lat": lat,
    "lon": lon,
}
yr_headers = {
    'User-Agent': 'learning_python',
    'From': 'nonworking@email.com',
}

endpoint = {
    "endpoint":yr_endpoint,
    "params": yr_param
}

answer = requests.get(endpoint["endpoint"], params=endpoint["params"], headers=yr_headers)
data = answer.json()
#data = data["properties"]["timeseries"]

print(json.dumps(data, indent=2))