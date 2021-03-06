import datetime
import json
from time import ctime

from time_data import time_data


def save_html(my_html, url):
    """Сохраняем текст страницы в html файл"""
    cryp_name = url.split("/")
    with open(f"saved_html/{cryp_name[-3]}.html", "w+", encoding="utf-8") as f:
        f.write(my_html)


def save_json_per_day(js, name):
    """Сохраняем json объект в json файл"""
    dt = str(datetime.datetime.now()).split(" ")
    tm = dt[1][:8].split(":")
    date = dt[0] + "-" + tm[0] + "-" + tm[1] + "-" + tm[2]
    with open(f"saved_json_per_day/{name}-{date}.json", "w+", encoding="utf-8") as f:
        json.dump(js, f, indent=4, ensure_ascii=False)
    print(f"Файл {name}-{date}.json готов!")


def save_json_per_hour(js, name, dt):
    """Сохраняем json объект в json файл"""
    if js["data"]["points"]:
        date = time_data(ctime(dt))
        with open(f"saved_json_per_hour/{name}-{date}.json", "w+", encoding="utf-8") as f:
            json.dump(js, f, indent=4, ensure_ascii=False)
        print(f"Файл {name}-{date}.json готов!")


def save_json_tass(js, start, end):
    """Сохраняем json объект в json файл"""
    s_date = time_data(ctime(start))
    e_date = time_data(ctime(end))
    with open(f"economica/news_list_{s_date}~{e_date}.json", "w+", encoding="utf-8") as f:
        json.dump(js, f, indent=4, ensure_ascii=False)
        print(f"Файл news_list_{s_date}~{e_date}.json готов!")
