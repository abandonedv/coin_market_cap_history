import pprint

import requests

URL = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=150000000&timeEnd=1648080000"


def get_json():
    return requests.get(URL).json()


def save_in_file(json):
    with open('crypto_history_files/test.txt', 'w+') as fp:
        fp.write(str(json))


def get_all_data(json):
    list_of_quotes = json["data"]["quotes"]
    for x in list_of_quotes:
        print(x)

