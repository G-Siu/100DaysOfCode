import requests
import os

BOT_TOKEN = os.environ["TELEGRAM_BOT_KEY"]
def telegram_bot_sendtext(bot_message):
    bot_token = BOT_TOKEN
    chat_id = os.environ["TELEGRAM_ID"]
    send_text = ("https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id="
                 + chat_id + "&parse_mode=Markdown&text=" + bot_message)

    bot_response = requests.get(send_text)

    return bot_response.json()


class NotificationManager:
    def send_alert(self, text):
        telegram_bot_sendtext(text)
