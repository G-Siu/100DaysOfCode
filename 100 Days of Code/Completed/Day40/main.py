from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

dt = DataManager()
sheet_data = dt.get_destination_data()
fs = FlightSearch()
nm = NotificationManager()


DEPARTURE_CITY = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = fs.destination_code(row["city"])
    dt.destination_data = sheet_data
    dt.update_destination_data()

tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=30*6)

for destination in sheet_data:

    flight = fs.check_flights(
        DEPARTURE_CITY,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months
    )
    if flight is None:
        continue
    print(f"{flight.destination_city}: £{flight.price}")
    if flight.price < sheet_data[0]["lowestPrice"]:
        users = dt.get_customer_emails()
        emails = [row["email"] for row in users]
        message = (f"Low price alert! Only £{flight.price} to fly from {flight.departure_city}-"
                      f"{flight.departure_airport} to {flight.destination_city}-{flight.destination_airport}, "
                      f"from {flight.out_date} to {flight.return_date}.")
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
    # nm.send_alert(message)
    nm.send_email(emails, message)
