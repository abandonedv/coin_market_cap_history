import datetime
import json


def save_html(my_html, url):
    cryp_name = url.split("/")
    with open(f"saved_html/{cryp_name[-3]}.html", "w+", encoding="utf-8") as f:
        f.write(my_html)


def save_json(js, name):
    dt = str(datetime.datetime.now()).split(" ")
    tm = dt[1][:8].split(":")
    date = dt[0] + "-" + tm[0] + "-" + tm[1] + "-" + tm[2]
    with open(f"saved_json/{name}-{date}.json", "w+", encoding="utf-8") as f:
        json.dump(js, f, indent=4, ensure_ascii=False)
    print(f"Файл {name}-{date}.json готов!")
