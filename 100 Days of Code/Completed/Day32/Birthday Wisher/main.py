import datetime as dt
import pandas as pd
import random
import smtplib

my_email = "garysiu.dev@gmail.com"
password = ""

current_day = dt.date.today()
today = (current_day.month, current_day.day)

data = pd.read_csv("birthdays.csv")
birthdays = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today in birthdays:
    birthday_person = birthdays[today]
    letter = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(letter) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}")
