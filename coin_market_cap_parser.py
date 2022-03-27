import pprint
import time
from time import sleep

import lxml
import requests
from bs4 import BeautifulSoup

from coin_market_cap_API import price_of_crypt, get_id_of_coin
from save_response import save_html, save_json, save_json_per_hour

COINS = []
URL = "https://coinmarketcap.com"
URL_HIST = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical"
URL_HIST_PER_HOUR = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail/chart"

HEADERS = {
    "accept": "application/json, text/plain, */*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
}

IDS = {'1': 'bitcoin',
       '1027': 'ethereum',
       '825': 'tether',
       '1839': 'bnb',
       '3408': 'usd-coin',
       '52': 'xrp',
       '2010': 'cardano',
       '5426': 'solana',
       '4172': 'terra-luna',
       '5805': 'avalanche',
       '6636': 'polkadot-new',
       '74': 'dogecoin',
       '4687': 'binance-usd',
       '7129': 'terrausd',
       '5994': 'shiba-inu',
       '3890': 'polygon',
       '3717': 'wrapped-bitcoin',
       '3635': 'cronos',
       '4943': 'multi-collateral-dai',
       '2': 'litecoin'}

END_OF_TIME = 1609448399
# 1514754000 - 01.01.2018
# 1577826000 = 01.01.2020
# 1609448400 - 01.01.2021
# 1640984400 - 01.01.2022


def get_html(url):
    """Получаем html страницу"""
    r = requests.get(url, headers=HEADERS)
    return r.text


def fill_list_of_ids_of_coins():
    """Создаем словарь,где ключ (id) это id криптовалюты на CMC, а значение - имя валюты"""
    coin_and_name_dict = {}
    for coin in COINS:
        id = get_id_of_coin(coin, "USD")
        coin_and_name_dict[id] = coin
    return coin_and_name_dict


def get_jsons_per_day(d):
    """Получаем json объекты где хранится история"""
    for id in d:
        parameters = {
            "id": id,
            "convertId": 2781,
            "timeStart": 1500000000,
            "timeEnd": 1648166400
        }
        js = requests.get(URL_HIST, params=parameters).json()
        # pprint.pprint(js)
        save_json(js, d[id])

def get_jsons_per_hour(d):
    """Получаем json объекты где хранится история"""
    time_start = 1577826000
    time_end = time_start + 86399
    for id in d:
        t_s = time_start
        t_e = time_end
        while t_e <= END_OF_TIME:
            print("*************************")
            print(time.ctime(t_s))
            my_range = str(t_s) + "~" + str(t_e)
            parameters = {
                "id": id,
                "range": my_range
            }
            js = requests.get(URL_HIST_PER_HOUR, params=parameters).json()
            # pprint.pprint(js)
            save_json_per_hour(js, d[id], t_s)
            t_s = t_e + 1
            t_e = t_s + 86399

def get_all_links(html):
    """Получаем ссылки на все криптовалюты с главной страницы и собираем в список"""
    soup = BeautifulSoup(html, "lxml")

    table = soup.find("table", class_="czTsgW")
    trs = table.find("tbody").find_all("tr", limit=20)
    links = []
    for tr in trs:
        a = tr.find("a").get("href")
        coin = a.split("/")[-2]
        COINS.append(coin)
        a = URL + a + "historical-data/"
        links.append(a)
    return links


def main():
    """Главная функция вызывающая все остальные"""
    # all_links = get_all_links(get_html(URL))
    # for url in all_links:
    #     my_html = get_html(url)
        # save_html(my_html, url)
    # d = fill_list_of_ids_of_coins()
    get_jsons_per_hour(IDS)


if __name__ == "__main__":
    main()
