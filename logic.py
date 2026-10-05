import requests
from bs4 import BeautifulSoup


result = requests.get("https://www.tgju.org/profile/price_dollar_rl")
soup = BeautifulSoup(result.text, "html.parser")

price = soup.select_one(
    'span[data-col="info.last_trade.PDrCotVal"]'
).text


price = list(price)
z=0
for i in price:
    if i==',':
        price.pop(z)
    price=price
    z+=1


pricee = ""    
for j in price:
    pricee+=j
    
        
pricee=int(pricee)  
print("shir")          
print(pricee//10)




