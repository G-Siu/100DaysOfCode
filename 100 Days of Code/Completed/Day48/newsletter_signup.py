from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.click()
first_name.send_keys("Gary")

last_name = driver.find_element(By.NAME, "lName")
last_name.click()
last_name.send_keys("Siu")

email = driver.find_element(By.NAME, "email")
email.click()
email.send_keys("garysiu@outlook.com")
email.send_keys(Keys.ENTER)
