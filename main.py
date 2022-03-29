import pprint
import requests

URL = "https://yandex.ru/news/rubric/business"

parametrs1 = {"page": 1,
              "prev-reqid": "1648449280677700-10438986447079637636-cxzbtdfagzijgz5u-BAL-3107-NEWS-NEWS_RUBRIC",
              "ajax": 1,
              "neo_parent_id": "1648449280677700-10438986447079637636-cxzbtdfagzijgz5u-BAL-3107-NEWS-NEWS_RUBRIC",
              "autoload": "%5B15%2C3%5D"}

parametrs2 = {"page": 2,
              "prev-reqid": "1648449296614946-5969224929367371555-b4cdtzh6jefk6hgl-BAL-3122-NEWS-NEWS_RUBRIC",
              "ajax": 1,
              "neo_parent_id": "1648449280677700-10438986447079637636-cxzbtdfagzijgz5u-BAL-3107-NEWS-NEWS_RUBRIC",
              "autoload": "%5B38%2C7%5D"}

parametrs3 = {"page": 2,
              "ajax": 1,
              "autoload": "%5B38%2C7%5D"}

parametrs4 = {"page": 2,
              "ajax": 1,
              "autoload": "%5B200%2C7%5D"}

r = requests.get(url=URL, params=parametrs4)
d = r.json()

pprint.pprint(d)
