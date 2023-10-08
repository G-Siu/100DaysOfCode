from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# driver.get(url="https://automatetheboringstuff.com")
# elem = driver.find_element(By.CSS_SELECTOR, "body > div > main > div > "
#                                             "ul:nth-child(24) > "
#                                             "li:nth-child(1) > a")
# elem.click()
# elems = driver.find_elements(By.CSS_SELECTOR, "p")
# print(len(elems))

# ----------------------------------------------------------
# driver.get(url="https://www.ebay.co.uk/")
# search_elem = driver.find_element(By.CSS_SELECTOR, "#gh-ac")
# search_elem.send_keys("Automate the Boring Stuff with Python")
# search_elem.submit()
# driver.back()
# driver.forward()
# driver.refresh()
# driver.quit()
# ----------------------------------------------------------
driver.get(url="https://automatetheboringstuff.com")
# elem = driver.find_element(By.CSS_SELECTOR, "body > div.main > main > div > "
#                                             "p:nth-child(14)")
# print(elem.text)

elem = driver.find_element(By.CSS_SELECTOR, "html")
print(elem.text)
