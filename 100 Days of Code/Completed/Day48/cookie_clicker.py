from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_id = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
runtime = time.time() + 60*5  # 5 minutes

while True:
    cookie.click()

    if time.time() > timeout:
        cost_tag = driver.find_elements(By.CSS_SELECTOR, "#store > div > b")
        cost = []
        # Get cost element tag and convert text to integer
        for price in cost_tag:
            cost_text = price.text
            if cost_text != "":
                cost.append(int(cost_text.split("-")[1].strip()
                                .replace(",", "")))
        # Dictionary of upgrades and cost
        upgrades = {}
        for i in range(len(cost)):
            upgrades[cost[i]] = items_id[i]
        # Get current number of cookies
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        money = int(money_element)
        # Check upgrades that are affordable
        can_upgrade = {}
        for price, ID in upgrades.items():
            if money > price:
                can_upgrade[price] = ID
        # Buy most expensive upgrade
        if len(can_upgrade) > 0:
            highest_upgradable = max(can_upgrade)
            print(highest_upgradable)
            to_buy_id = can_upgrade[highest_upgradable]
            driver.find_element(By.ID, to_buy_id).click()

        # Add 5 seconds from current time for next upgrades check
        timeout = time.time() + 5
    # Check 5 minute mark to end game and get cookies per second count
    if time.time() > runtime:
        cookies_second = driver.find_element(By.ID, "cps").text
        print(cookies_second)
        break
