import requests
from datetime import datetime

MY_LAT = 55.883787
MY_LNG = -4.334450

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0  # Changes time format from AM/PM to UNIX
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()  # Will raise status code 400 if no parameters are provided to this API

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now)
