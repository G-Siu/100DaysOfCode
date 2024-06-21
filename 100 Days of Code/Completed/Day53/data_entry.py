import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

FORM = "https://forms.gle/5LT4En8ckdPshb349"

r = requests.get("https://appbrewery.github.io/Zillow-Clone/")
# print(r.status_code)

soup = BeautifulSoup(r.text,
                     "html.parser")

# print(soup.prettify())

raw_addresses = soup.find_all("address")
addresses = [address.text.strip().replace(" |", ",") for address in
             raw_addresses]
# print(addresses)

raw_prices = soup.find_all("span",
                           class_="PropertyCardWrapper__StyledPriceLine")
prices = [price.text.rstrip("+/mo").rstrip("+ 1bd") for price in raw_prices]
# print(prices)

raw_links = soup.find_all("a", class_="property-card-link")
links = [link["href"] for link in raw_links]
# print(links)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


for index in range(len(addresses)):
    driver.get(FORM)
    time.sleep(2)

    address_input = driver.find_element(By.CSS_SELECTOR, "div > input["
                                                            "type='text']")
    address_input.click()
    address_input.send_keys(addresses[index])

    price_input = driver.find_element(By.XPATH,
                                      "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_input.click()
    price_input.send_keys(prices[index])

    link_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_input.click()
    link_input.send_keys(links[index])

    driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div["
                                  "1]/div[1]/div/span/span").click()
    time.sleep(2)
