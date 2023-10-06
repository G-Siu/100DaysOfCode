import requests

BOT_TOKEN = ""
MY_LAT = 55.883787
MY_LNG = -4.334450
# API_KEY = ""
API_KEY = ""  # Borrowed API key
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"


def telegram_bot_sendtext(bot_message):
    bot_token = BOT_TOKEN
    chat_id = ""
    send_text = ("https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id="
                 + chat_id + "&parse_mode=Markdown&text=" + bot_message)

    bot_response = requests.get(send_text)

    return bot_response.json()


parameter = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(url=OWM_Endpoint, params=parameter)
response.raise_for_status()
# print(response.status_code)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
condition_code = [hour_data["weather"][0]["id"] for hour_data in weather_slice]
for hour in condition_code:
    if int(hour) < 700:
        will_rain = True

if will_rain:
    telegram_bot_sendtext("Bring an umbrella.")
