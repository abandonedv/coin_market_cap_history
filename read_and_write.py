import pprint
import json
import os
import write_into_csv

PATH = "/home/ludwig/Documents/GitHub/test_parsing/saved_json"


class hist_data():
    def __init__(self, name, day_data):
        self.coin_parse = name
        self.coin_time = day_data["timeClose"][:10]
        self.coin_value = day_data["quote"]["close"]


def get_js_from_file(file):
    with open("saved_json/" + file, 'r') as f:
        js = json.load(f)
        return js


def get_all_data(json):
    history_of_coin = []
    list_of_quotes = json["data"]["quotes"]
    name_of_coin = json["data"]["name"]
    for day_data in list_of_quotes:
        # pprint.pprint(day_data)
        history_of_coin.append(hist_data(name_of_coin, day_data))
    return history_of_coin


def main():
    files = os.listdir(PATH)
    write_into_csv.create()
    for file in files:
        js = get_js_from_file(file)
        l = get_all_data(js)
        write_into_csv.insert(l)
        # db.insert...


if __name__ == "__main__":
    main()
