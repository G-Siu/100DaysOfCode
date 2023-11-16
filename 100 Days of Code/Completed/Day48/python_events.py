from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

time = driver.find_elements(By.CSS_SELECTOR,
                            value=".event-widget div ul li time")

event = driver.find_elements(By.CSS_SELECTOR,
                             value=".event-widget div ul a")

# print(time[0].text)
# print(event[0].text)
event_times = [date.text for date in time]
event_names = [text.text for text in event]
# print(time_dict)
# print(event_list)
events = {}
for i in range(len(event_times)):
    events[i] = {
        "times": event_times[i],
        "names": event_names[i],
    }
print(events)

driver.quit()
