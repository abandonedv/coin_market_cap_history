import requests
from bs4 import BeautifulSoup
from selenium import webdriver

URL = "https://coinmarketcap.com/currencies/bitcoin/markets/"


p = requests.get(URL)
h = p.text
soup = BeautifulSoup(h, "lxml")
s = soup.find_all("div", class_="sc-16r8icm-0 jKrmxw container")[0]
print(s.prettify())
