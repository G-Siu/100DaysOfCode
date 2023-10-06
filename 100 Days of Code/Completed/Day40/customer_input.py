import requests
import os

TOKEN = os.environ["SHEETY_BEARER"]

print("Welcome to Gary's Flight Club\nWe find the best flight deals and email you.")
first_name = input("What is your first name?\n").title()
last_name = input("What is your last name?\n").title()
email = "1"
email2 = "2"
while email != email2:
    email = input("What is your email?\n")
    email2 = input("Type your email again?\n")
    if email == email2:
        print("You're in the club!")
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}
parameters = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
    }
}

r = requests.post(url=f"https://api.sheety.co/{os.environ['SHEETY_USERNAME']}/flightDeals/users",
                  headers=headers, json=parameters)
r.raise_for_status()
