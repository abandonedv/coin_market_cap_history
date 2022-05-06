import time

import requests
from bs4 import BeautifulSoup

from coin_market_cap_api import get_id_of_coin
from save_response import save_json_per_day, save_json_per_hour
from time_const import *

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


def get_html(url):
    """Получаем html страницу"""
    r = requests.get(url, headers=HEADERS)
    return r.text


def fill_list_of_ids_of_coins(coins):
    """Создаем словарь,где ключ (id) это id криптовалюты на CMC, а значение - имя валюты"""
    coin_and_name_dict = {}
    for coin in coins:
        id = get_id_of_coin(coin, "USD")
        coin_and_name_dict[id] = coin
    return coin_and_name_dict


def get_jsons_per_day(ids_and_names):
    """Получаем json объекты где хранится история"""
    for id in ids_and_names:
        parameters = {
            "id": id,
            "convertId": 2781,
            "timeStart": TIME_01_01_2019,
            "timeEnd": TIME_01_01_2020 - 1
        }
        js = requests.get(URL_HIST, params=parameters).json()
        # pprint.pprint(js)
        save_json_per_day(js, ids_and_names[id])


def get_jsons_per_hour(ids_and_names):
    """Получаем json объекты где хранится история"""
    end_of_time = TIME_01_01_2020 - 1
    time_start = TIME_01_01_2019
    for id in ids_and_names:
        t_s = time_start
        t_e = time_start + DAY - 1
        while t_e <= end_of_time:
            print("*************************")
            print(time.ctime(t_s))
            my_range = str(t_s) + "~" + str(t_e)
            parameters = {
                "id": id,
                "range": my_range
            }
            my_json = requests.get(URL_HIST_PER_HOUR, params=parameters).json()
            # pprint.pprint(js)
            save_json_per_hour(my_json, ids_and_names[id], t_s)
            t_s = t_e + 1
            t_e = t_s + DAY - 1


def get_all_links(html):
    """Получаем ссылки на все криптовалюты с главной страницы и собираем в список"""
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", class_="czTsgW")
    trs = table.find("tbody").find_all("tr", limit=20)
    names_of_coins = []
    for tr in trs:
        a = tr.find("a").get("href")
        coin = a.split("/")[-2]
        names_of_coins.append(coin)
    return names_of_coins


def main():
    """Главная функция вызывающая все остальные"""
    # coins = get_all_links(get_html(URL))
    # ids_and_names = fill_list_of_ids_of_coins(coins)
    get_jsons_per_hour(IDS)


if __name__ == "__main__":
    main()
