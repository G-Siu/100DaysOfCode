# import smtplib
#
# my_email = "garysiu@outlook.com"
# password = "wtiktygimhhmvtyv"
# with smtplib.SMTP("outlook.office365.com", port=587) as connection:
#     connection.starttls()  # Transport Layer Security, a form of encryption
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="garysiu_888@hotmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email")


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# # print(type(year))
# # print(day_of_week)
#
# date_of_birth = dt.datetime(year=1992 , month=1 , day=28)  # Default hour parameter as midnight
# print(date_of_birth)
#

import datetime as dt
import random
import smtplib


my_email = "garysiu@outlook.com"
password = ""

current_day = dt.datetime.now()
weekday = current_day.weekday()
if weekday == 6:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
        print(quote)
    with smtplib.SMTP("outlook.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Monday Motivation\n\n{quote}")
