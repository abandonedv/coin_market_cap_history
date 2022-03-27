import datetime
import json
from time import ctime


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
    with open(f"saved_json/{name}-{date}.json", "w+", encoding="utf-8") as f:
        json.dump(js, f, indent=4, ensure_ascii=False)
    print(f"Файл {name}-{date}.json готов!")


def save_json_per_hour(js, name, dt):
    """Сохраняем json объект в json файл"""
    if js["data"]["points"]:
        d = ctime(dt)
        date = d[-4:] + "-" + d[4:7] + "-" + (d[8:10]).split(" ")[-1]
        with open(f"test/{name}-{date}.json", "w+", encoding="utf-8") as f:
            json.dump(js, f, indent=4, ensure_ascii=False)
        print(f"Файл {name}-{date}.json готов!")
