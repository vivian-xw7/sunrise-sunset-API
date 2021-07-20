import requests
from datetime import datetime


MY_LAT = 38.883530
MY_LONG = -94.818237

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

# Olathe has 7 hour difference from UTC
print(int(sunrise) + 7)
print(int(sunset) + 7)

time_now = datetime.now()
print(time_now.hour)
