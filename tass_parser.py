import pprint
import json
import time
from save_response import save_json_tass
import requests
import lxml
from bs4 import BeautifulSoup

URL_TASS = "https://tass.ru/rubric/api/v1/rubric-articles"

HEADERS = {"accept": "application/json, text/plain, */*",
           "accept-encoding": "gzip, deflate, br",
           "accept-language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7",
           "content-type": "application/json;charset=utf-8",
           "cookie": "__jhash_=255; __jua_=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 YaBrowser/22.3.2.644 Yowser/2.5 Safari/537.36; __js_p_=364,1800,0,0; __hash_=b3447df5fa7dcf2176a04242d4e784d3; __lhash_=983c9cb9e698150f575471b0c92ba0f4; tass_uuid=63043B4B-B39E-4B99-B263-6EF6A7E15519; _ym_uid=1650307369506415155; _ym_d=1650307369; _ym_isad=1; _ym_visorc=b",
           "referer": "https://tass.ru/mezhdunarodnaya-panorama",
           "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
           "sec-ch-ua-mobile": "?0",
           "sec-ch-ua-platform": "Windows",
           "sec-fetch-dest": "empty",
           "sec-fetch-mode": "cors",
           "sec-fetch-site": "same-origin",
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"}


def get_json():
    """Получаем json объекты где хранится история"""
    parametrs_time = 1525793261
    while parametrs_time > 1514754000:
        parametrs_tass = {"slug": "mezhdunarodnaya-panorama",
                          "type": "all",
                          "tuplesLimit": "20",
                          "lastDate": parametrs_time}
        my_json = requests.get(url=URL_TASS, params=parametrs_tass, headers=HEADERS).json()
        news = my_json["data"]["news"]
        start_time = news[0][0]["publishDate"]
        end_time = news[-1][0]["publishDate"]
        save_json_tass(my_json, start_time, end_time)
        parametrs_time = end_time - 1
        print("* " + str(parametrs_time))


def main():
    get_json()


if __name__ == "__main__":
    main()
