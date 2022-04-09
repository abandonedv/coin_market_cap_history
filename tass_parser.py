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
           "cookie": "__lhash_=f929dab8815b9dfe68a04b9d795bbc99; _ym_uid=1648672059560556898; _ym_d=1648672059; top100_id=t1.2706484.575019607.1648672058921; adtech_uid=212a5368-f009-4187-b58a-03d29c5ffef2:tass.ru; user-id_1.0.5_lr_lruid=pQ8AADu9RGJoiJprAUb2kgA=; _ym_isad=2; _ym_visorc=b; tass_uuid=3BD140F8-6F2B-40B6-80DC-A4EC7F1C4929; __js_p_=414,1800,0,0; __jhash_=208; __jua_=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36; __hash_=1813772e2748c86eda8634888bfd43d0; last_visit=1648663630758::1648674430758; newsListCounter=1; t1_sid_2706484=s1.635826780.1648672058922.1648674463958.1.22.22",
           "referer": "https://tass.ru/politika",
           "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
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
        parametrs_tass = {"slug": "politika",
                          "type": "all",
                          "step": "NaN",
                          "tuplesLimit": "20",
                          "lastDate": parametrs_time}
        my_json = requests.get(url=URL_TASS, params=parametrs_tass, headers=h).json()
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
