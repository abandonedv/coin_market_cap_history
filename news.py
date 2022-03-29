import pprint
import json
import requests
import lxml
from bs4 import BeautifulSoup

URL = "https://tass.ru/rubric/api/v1/rubric-articles"
URL_CMC = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail/chart"
"slug=politika&type=all&step=NaN&tuplesLimit=20&lastDate=1540000000&newsOffset=20"

parametrs_tass = {"slug": "politika",
                  "type": "all",
                  "step": "NaN",
                  "tuplesLimit": 20,
                  "lastDate": 1540000000,
                  "newsOffset": 40}

parametrs_cmc = {"id": 1,
                 "range": "1646168400~1646427599"}

HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.3.954 (beta) Yowser/2.5 Safari/537.36"}

my_html = requests.get(url=URL, params=parametrs_tass, headers=HEADERS).text
soup = BeautifulSoup(my_html, "lxml")
pre = soup.find("pre")

pprint.pprint()
