import requests
from bs4 import BeautifulSoup
from selenium import webdriver

URL = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=150000000&timeEnd=1648080000"


p = requests.get(URL)
print(p)
# h = p.text
# soup = BeautifulSoup(h, "lxml")
# s = soup.find_all("div", class_="sc-16r8icm-0 jKrmxw container")[0]
# print(s.prettify())
