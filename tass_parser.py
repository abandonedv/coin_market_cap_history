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
    "cookie": "__lhash_=d7666ad10e1a3ef15781ff9f26ad1313; _ym_d=1648573603; _ym_uid=164857360362684008; _ym_isad=2; adtech_uid=3ba67a7a-8ecb-4b5a-9637-149f7f09f11c:tass.ru; user-id_1.0.5_lr_lruid=pQ8AAF1OQ2JOVKPcAaUEKQA=; chash=Ce6Sir9L0S; top100_id=t1.2706484.1866749024.1648581352546; last_visit=1648570552551::1648581352551; t1_sid_2706484=s1.1143615218.1648581352548.1648581361991.1.3.3; __jua_=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36; _ym_visorc=b; tass_uuid=85C54A88-2ED4-410C-85B8-0102F684E0C4; newsListCounter=61; __js_p_=68,1800,0,0; __jhash_=1049; __hash_=18579752bd444e279acefca041a5a5f8",
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
    parametrs_time = 1648590735
    while parametrs_time > 1640984400:
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