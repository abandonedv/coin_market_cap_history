import pprint
import json
import os
import write_into_csv

PATH = "/home/ludwig/Documents/GitHub/test_parsing/saved_json"


class Date_data():
    """Класc для удобного представления необходимых мне данных"""
    def __init__(self, name, day_data):
        self.coin_parse = name
        self.coin_time = day_data["timeClose"][:10]
        self.coin_value = day_data["quote"]["close"]


def get_js_from_file(file):
    """Извлекаем json объект из json файла"""
    with open("saved_json/" + file, 'r') as f:
        js = json.load(f)
        return js


def get_all_data(json):
    """Создаем список объектов date_data"""
    history_of_coin = []
    list_of_quotes = json["data"]["quotes"]
    name_of_coin = json["data"]["name"]
    for day_data in list_of_quotes:
        # pprint.pprint(day_data)
        history_of_coin.append(Date_data(name_of_coin, day_data))
    return history_of_coin


def main():
    """Главная функция вызывающая все остальные"""
    files = os.listdir(PATH)
    write_into_csv.create()
    for file in files:
        js = get_js_from_file(file)
        l = get_all_data(js)
        write_into_csv.insert(l)
        # db.insert...


if __name__ == "__main__":
    main()
