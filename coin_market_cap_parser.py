import pprint
from time import sleep

import lxml
import requests
from bs4 import BeautifulSoup

from coin_market_cap_API import price_of_crypt, get_id_of_coin
from save_response import save_html, save_json

COINS = []
URL = "https://coinmarketcap.com"
URL_HIST = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical"

HEADERS = {
    "accept": "application/json, text/plain, */*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
}


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


def get_jsons(d):
    """Получаем json объекты где хранится история"""
    for id in d:
        parameters = {
            "id": id,
            "convertId": 2781,
            "timeStart": 150000000,
            "timeEnd": 1648166400
        }
        js = requests.get(URL_HIST, params=parameters).json()
        # pprint.pprint(js)
        save_json(js, d[id])


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
    all_links = get_all_links(get_html(URL))
    # for url in all_links:
    #     my_html = get_html(url)
        # save_html(my_html, url)
    d = fill_list_of_ids_of_coins()
    get_jsons(d)


if __name__ == "__main__":
    main()
