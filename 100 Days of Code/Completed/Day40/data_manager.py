import requests
import os
from pprint import pprint

RETRIEVE_ENDPOINT = f"https://api.sheety.co/{os.environ['SHEETY_USERNAME']}/flightDeals/prices"
USERS_ENDPOINT = f"https://api.sheety.co/{os.environ['SHEETY_USERNAME']}/flightDeals/users"

class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        # Sheety API to get data within sheet
        header = {
            "Authorization": f"Bearer {os.environ['SHEETY_BEARER']}"
        }
        r = requests.get(url=RETRIEVE_ENDPOINT, headers=header)
        data = r.json()
        # pprint(data)  # Prints the json in a more readable format
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            r = requests.put(url=f"{RETRIEVE_ENDPOINT}/{city['id']}", json=new_data)
            # print(r.text)

    def get_customer_emails(self):
        header = {
            "Authorization": f"Bearer {os.environ['SHEETY_BEARER']}"
        }
        customers_endpoint = USERS_ENDPOINT
        r = requests.get(customers_endpoint, headers=header)
        data = r.json()
        self.customer_data = data["users"]
        return self.customer_data
