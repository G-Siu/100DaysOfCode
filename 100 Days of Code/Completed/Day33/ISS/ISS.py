import requests
from datetime import datetime
import smtplib
import time

MY_LNG = -4.334450
MY_LAT = 55.883787

MY_EMAIL = "garysiu.dev@gmail.com"
PASSWORD = ""


# Check if ISS position is +-5 degrees to my position
def in_position():
    # Get ISS longitude and latitude
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    position_iss = (longitude, latitude)

    if (MY_LNG-5) <= longitude <= (MY_LNG+5) and (MY_LAT-5) <= latitude <= (MY_LAT+5):
        return True


def is_dark():
    # Get sunrise and sunset based on longitude and latitude
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0  # Changes time format from AM/PM to UNIX
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()  # Will raise status code 400 if no parameters are provided to this API

    data = response.json()
    # Check sunrise and sunset hours
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if sunset <= time_now.hour <= sunrise:
        return True


# Send email when ISS in position and my location is dark
while True:
    time.sleep(60)
    if in_position() and is_dark():
        with smtplib.SMTP("outlook.office365.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:ISS in position\n\nLOOK UP TO SEE ISS!"
            )

# If ISS is close to my current position
# And is currently dark
# Then send an email to lookup
# BONUS: run code every 60 seconds
