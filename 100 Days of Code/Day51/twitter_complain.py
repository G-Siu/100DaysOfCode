from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

PROMISED_DOWN = 455
PROMISED_UP = 455

TWITTER_EMAIL = "garysiu.dev@gmail.com"
TWITTER_PASSWORD = "gazawaza28"


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.implicitly_wait(4)
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        self.driver.find_element(By.CLASS_NAME, "start-text").click()
        wait = WebDriverWait(self.driver, timeout=60)
        wait.until_not(EC.presence_of_element_located((
            By.PARTIAL_LINK_TEXT, "Result ID")))
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        self.down = self.driver.find_element(By.CLASS_NAME,
                                             "download-speed").text
        print(self.up, self.down)

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
