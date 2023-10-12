from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles_tag = driver.find_element(By.CSS_SELECTOR,
#                                    value="#articlecount > a:nth-child(1)")
# articles_tag.click()

# total_articles = articles_tag.text
# print(total_articles)

# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()


# driver.quit()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
