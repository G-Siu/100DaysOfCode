import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/"
TEQUILA_SEARCH = "https://api.tequila.kiwi.com/v2"
API_key = "A6stMMTaQoa7sj_2AjST203aqwTbzreM"


class FlightSearch:
    def destination_code(self, city):
        # Return destination IATA code
        headers = {"apikey": API_key}
        query = {
            "term": city,
            "location_types": "city"
        }
        r = requests.get(url=f"{TEQUILA_ENDPOINT}locations/query", headers=headers, params=query)
        results = r.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, departure_city, destination_city, from_time, to_time):
        headers = {
            "apikey": API_key,
        }
        query = {
            "fly_from": departure_city,
            "fly_to": destination_city,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        r = requests.get(url=f"{TEQUILA_SEARCH}/search", headers=headers, params=query)
        try:
            data = r.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city}.")
            return None
        fd = FlightData(
            price=data["price"],
            departure_city=data["route"][0]["cityFrom"],
            departure_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        return fd
