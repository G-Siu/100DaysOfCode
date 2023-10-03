import requests
from datetime import date, timedelta

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

AV_API_KEY = ""
NEWS_API_KEY = ""

BOT_TOKEN = ""


def telegram_bot_sendtext(bot_message):
    bot_token = BOT_TOKEN
    chat_id = ""
    send_text = ("https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id="
                 + chat_id + "&parse_mode=Markdown&text=" + bot_message)

    bot_response = requests.get(send_text)

    return bot_response.json()


params_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": AV_API_KEY
}
# Get yesterday and day before dates
today = date.today()
yesterday = str(today - timedelta(days=1))
day_before = str(today - timedelta(days=2))
# Get tesla stock data
r = requests.get(url=STOCK_ENDPOINT, params=params_stock)
r.raise_for_status()

tesla_data = r.json()
yesterday_price = tesla_data["Time Series (Daily)"][yesterday]
yesterday_close = [value for (key, value) in yesterday_price.items()][3]  # Yesterday's closing price
try:
    day_before_price = tesla_data["Time Series (Daily)"][day_before]
    day_before_close = [value for (key, value) in day_before_price.items()][3]
except KeyError:
    day_before = str(today - timedelta(days=4))
    day_before_price = tesla_data["Time Series (Daily)"][day_before]
    day_before_close = [value for (key, value) in day_before_price.items()][3]

price_diff = abs(float(yesterday_close) - float(day_before_close))
up_down = None
if price_diff > 0:
    up_down = "🔺️"
else:
    up_down = "🔻"
# Percentage difference
percentage_diff = round((price_diff / float(day_before_close)) * 100)

params_news = {
    "q": COMPANY_NAME,
    # "qInTitle": COMPANY_NAME,
    "from": day_before,
    "to": yesterday,
    "language": "en",
    "apiKey": NEWS_API_KEY
}
if percentage_diff > 0.1:
    r = requests.get(url=NEWS_ENDPOINT, params=params_news)
    r.raise_for_status()

    news_data = r.json()
    # print(news_data)
    latest_news = news_data["articles"][:3]
    # print(latest_news)

# Take headlines and format into list
formatted_news = [f"{STOCK_NAME}: {up_down}{percentage_diff}%\nHeadline: {article['title']}" for article in latest_news]

for article in formatted_news:
    telegram_bot_sendtext(article)

