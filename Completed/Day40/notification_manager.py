import requests
import os
import smtplib

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

    def send_email(self, emails, text):
        my_email = "garysiu@outlook.com"
        password = "kmhqaidkdqfevvwa"
        with smtplib.SMTP("outlook.office365.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for email in emails:
                connection.sendmail(from_addr=my_email,
                                    to_addrs=email,
                                    msg=f"Subject:Cheap Flights!\n\n{text}".encode('utf-8'))