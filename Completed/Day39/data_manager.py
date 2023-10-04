import requests
from pprint import pprint

RETRIEVE_ENDPOINT = "https://api.sheety.co/3dbfe1f109be8ab861bbb4646c950d9c/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # Sheety API to get data within sheet
        r = requests.get(url=RETRIEVE_ENDPOINT)
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