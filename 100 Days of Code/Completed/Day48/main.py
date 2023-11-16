from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.co.uk/TP-Link-TL-PA7027P-KIT-Passthrough"
#            "-Configuration/dp/B08DVGRQ59/ref=sr_1_3?crid=2GTYIVSVYKV24"
#            "&keywords=tp-link%2Bav1000&qid=1697037223&s=computers&sprefix=tp"
#            "-link%2Bav1000%2Ccomputers%2C136&sr=1-3&th=1")

# price_pound = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_pence = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_pound.text}.{price_pence.text}")

driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)  # Easy to get tag from identifiers
# print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
# print(button.size)
documentation_link = driver.find_element(By.CSS_SELECTOR,
                                         value=".documentation-widget a")
# print(documentation_link.text)  # CSS Selector can be used where
# identifiers are absent

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div['
                                         '2]/div/ul/li['
                                    '3]/a')
# print(bug_link.text)  # Can use XPATH
# driver.close()  # Closes the active tab
driver.quit()  # Closes all of Chrome
