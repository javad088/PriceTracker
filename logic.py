import requests
from bs4 import BeautifulSoup


result = requests.get("https://www.tgju.org/profile/price_dollar_rl")
soup = BeautifulSoup(result.text, "html.parser")

price = soup.select_one(
    'span[data-col="info.last_trade.PDrCotVal"]'
).text

print(price)