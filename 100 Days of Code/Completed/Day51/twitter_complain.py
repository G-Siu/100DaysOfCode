from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

PROMISED_DOWN = 455
PROMISED_UP = 455

TWITTER_USERNAME = "DevGazS"
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
        wait = WebDriverWait(self.driver, timeout=90)
        wait.until_not(EC.text_to_be_present_in_element_attribute((
            By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div["
                      "2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div["
                      "2]/div/div[2]/span"), "data-upload-status-value", "NaN"))
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        self.down = self.driver.find_element(By.CLASS_NAME,
                                             "download-speed").text

    def tweet_at_provider(self):
        if float(self.down) < PROMISED_DOWN or float(self.up) < PROMISED_UP:
            self.driver.get("https://x.com/?lang=en-gb")
            self.driver.implicitly_wait(4)
            self.driver.find_element(By.LINK_TEXT, "Sign in").click()
            self.driver.implicitly_wait(4)
            user_input = self.driver.find_element(By.NAME, "text")
            user_input.click()
            user_input.send_keys(TWITTER_USERNAME)
            self.driver.find_element(By.XPATH,
                                     "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span").click()
            self.driver.implicitly_wait(2)
            if self.driver.find_element(By.XPATH, "//*[@id='modal-header']/span/span"):
                try:
                    captcha = self.driver.find_element(By.XPATH,
                                                       "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
                    captcha.click()
                    captcha.send_keys(TWITTER_EMAIL)
                    captcha.send_keys(u'\ue007')  # Press Enter
                except:
                    print("No captcha")
            self.driver.implicitly_wait(4)
            password_input = self.driver.find_element(By.CSS_SELECTOR, "#layers > div:nth-child(2) > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-kemksi.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-175oi2r.r-1e084wi.r-13qz1uu > div > label > div > div.css-175oi2r.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-is05cd.r-ttdzmv > div.css-146c3p1.r-bcqeeo.r-1ttztb7.r-qvutc0.r-37j5jr.r-135wba7.r-16dba41.r-1awozwy.r-6koalj.r-1inkyih.r-13qz1uu > input")
            password_input.click()
            password_input.send_keys(TWITTER_PASSWORD)
            password_input.send_keys(u'\ue007')  # Press Enter
            wait = WebDriverWait(self.driver, timeout=10)
            wait.until(EC.presence_of_element_located((By.XPATH,
                                                      "//*["
                                                      "@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div")))
            tweet = self.driver.find_element(By.XPATH, "//*["
                                                 "@id='react-root']/div/div/div["
                                              "2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
            tweet.click()
            tweet.send_keys(f"Hey ISP, why is my internet speed {self.down} "
                            f"download / {self.up} upload when I pay for 900 "
                            f"download / 900 upload?")
            self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span").click()
            print("Posted complaint!")
        else:
            print("Speeds are fine!")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
