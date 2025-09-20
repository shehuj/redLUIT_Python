import requests

city = "Dallas"
# You need to sign up for a free API key at https://www.weatherapi.com/
# Replace the key below with your own key.
url = "http://api.weatherapi.com/v1/current.json?key=b9328b5b42634685935201729251909&q=[city]&aqi=no"

response = requests.get(url)
weather_json = response.json()

temp = weather_json.get("current").get("temp_f")
description = weather_json.get("current").get("condition").get("text")

print("Today's weather in", city, "is", description, "with a temperature of", temp, "F")

