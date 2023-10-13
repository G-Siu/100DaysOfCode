from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

# def abort_application():
#     # Click Close Button
#     close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
#     close_button.click()
#
#     time.sleep(2)
#     # Click Discard Button
#     discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
#     discard_button.click()

USERNAME = ""
PASSWORD = ""
# PHONE = ""

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3716303087"
           "&f_AL=true&geoId=102257491&keywords=python%20developer&location"
           "=London%2C%20England%2C%20United%20Kingdom&origin"
           "=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true&sortBy=R")

# Reject cookies
time.sleep(2)
reject_button = driver.find_element(By.CSS_SELECTOR, 'button['
                                                     'action-type="DENY"]')
reject_button.click()

# Sign in button
time.sleep(1)
sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

# Sign in page
time.sleep(2)
username_login = driver.find_element(By.ID, "username")
password_login = driver.find_element(By.ID, "password")
username_login.send_keys(USERNAME)
password_login.send_keys(PASSWORD)
password_login.send_keys(Keys.ENTER)

# In case of CAPTCHA
# input("Press Enter once CAPTCHA solved")

# Job listings
time.sleep(3)
jobs_tag = driver.find_elements(By.CSS_SELECTOR,
                                ".job-card-container--clickable")
for i in range(len(jobs_tag)):
    job = jobs_tag[i]
    job.click()
    time.sleep(1)
    save = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save.click()

# To apply to jobs
# for i in jobs_tag:
#     i.click()
#     time.sleep(1)
#     try:
#         # Apply button
#         apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
#         apply_button.click()
#
#         # Insert Phone Number
#         # Find an <input> element where the id contains phoneNumber
#         time.sleep(3)
#         phone = driver.find_element(By.CSS_SELECTOR,"input[id*=phoneNumber]")
#         if phone.text == "":
#             phone.send_keys(PHONE)
#
#         # Check the Submit Button
#         submit_button = driver.find_element(By.CSS_SELECTOR,"footer button")
#         if submit_button.get_attribute("data-control-name") == "continue_unify":
#             abort_application()
#             print("Complex application, skipped.")
#             continue
#         else:
#             # Click Submit Button
#             print("Submitting job application")
#             submit_button.click()
#         time.sleep(1)
#         # Click Close Button
#         close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
#         close_button.click()
#     except NoSuchElementException:
#         abort_application()
#         print("No application button, skipped.")
#         continue