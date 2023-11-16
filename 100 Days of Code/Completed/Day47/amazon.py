import requests
from bs4 import BeautifulSoup
import smtplib
import os

EMAIL = ""
password = os.environ["OUTLOOK_KEY"]

TARGET_PRICE = 50
URL = ("https://www.amazon.co.uk/TP-Link-TL-PA7027P-KIT-Passthrough"
       "-Configuration/dp/B08DVGRQ59/ref=sr_1_3?crid=2GTYIVSVYKV24&keywords"
       "=tp-link%2Bav1000&qid=1697037223&s=computers&sprefix=tp-link"
       "%2Bav1000%2Ccomputers%2C136&sr=1-3&th=1")

headers = {
    "User-Agent": "",
    "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8,ja;q=0.7",
}  # Get from https://myhttpheader.com/

r = requests.get(url=URL, headers=headers)
# print(r.content)  # Check html is requested correctly

soup = BeautifulSoup(r.content, "html.parser")
# print(soup.prettify(encoding="utf-8"))

price_tag = soup.find(name="span", class_="a-offscreen")
price = price_tag.text
# print(price)
price_float = float(price.replace("£", ""))

title = soup.find(id="productTitle").get_text().strip()
# print(title)

if price_float < TARGET_PRICE:
    message = f"{title} is now {price}\n"
    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=password)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                            msg=f"Subject: Amazon Price Alert\n\n"
                                f"{message}{URL}".encode("utf-8"))
