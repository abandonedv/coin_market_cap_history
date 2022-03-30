import pprint
import json
import time
from save_response import save_json_tass
import requests
import lxml
from bs4 import BeautifulSoup

URL_TASS = "https://tass.ru/rubric/api/v1/rubric-articles"

HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7",
    "content-type": "application/json;charset=utf-8",
    "cookie": "__lhash_=d7666ad10e1a3ef15781ff9f26ad1313; _ym_d=1648573603; _ym_uid=164857360362684008; _ym_isad=2; adtech_uid=3ba67a7a-8ecb-4b5a-9637-149f7f09f11c:tass.ru; user-id_1.0.5_lr_lruid=pQ8AAF1OQ2JOVKPcAaUEKQA=; chash=Ce6Sir9L0S; top100_id=t1.2706484.1866749024.1648581352546; __js_p_=227,1800,0,0; __jhash_=223; __jua_=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36; _ym_visorc=b; last_visit=1648624437132::1648635237132; t1_sid_2706484=s1.118301340.1648635237128.1648635248063.3.3.12; __hash_=b9e8592113d5e2e5afc54f5c9df1fdd5; tass_uuid=4D7B7D3C-1780-4CE3-8A43-434E41BBDA67; newsListCounter=0",
    "referer": "https://tass.ru/politika",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"}


def get_json():
    """Получаем json объекты где хранится история"""
    parametrs_time = 1525793261
    while parametrs_time > 1514754000:
        parametrs_tass = {"slug": "politika",
                          "type": "all",
                          "tuplesLimit": 500,
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