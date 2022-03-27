import pprint
import json
import os
import time

import write_into_csv
import my_dbase

PATH_OF_PER_DAY = "saved_json_per_day"
PATH_OF_PER_HOUR = "saved_json_per_hour"


class Date_data_per_day():
    """Класc для удобного представления необходимых мне данных"""

    def __init__(self, name, day_data):
        self.coin_parse = name
        self.coin_time = day_data["timeClose"][:10]
        self.coin_value = day_data["quote"]["close"]


class Date_data_per_hour():
    """Класc для удобного представления необходимых мне данных"""

    def __init__(self, name, coin_time, coin_value):
        self.coin_parse = name
        self.coin_time = coin_time
        self.coin_value = coin_value


def get_js_from_file(file):
    """Извлекаем json объект из json файла"""
    with open(PATH_OF_PER_HOUR + "/" + file, 'r') as f:
        js = json.load(f)
        name = file.split("-")[0]
        return js, name


def get_all_data_per_day(my_js):
    """Создаем список объектов date_data"""
    history_of_coin = []
    list_of_quotes = my_js["data"]["quotes"]
    name_of_coin = my_js["data"]["name"]
    for day_data in list_of_quotes:
        # pprint.pprint(day_data)
        history_of_coin.append(Date_data_per_day(name_of_coin, day_data))
    return history_of_coin


def get_all_data_per_hour(my_js, name_of_coin):
    """Создаем список объектов date_data"""
    history_of_coin = []
    list_of_points = my_js["data"]["points"]
    last_time = 0
    for my_time in list_of_points:
        my_t = int(my_time)
        if last_time + 3600 <= my_t:
            last_time = my_t
            # pprint.pprint(day_data)
            history_of_coin.append(Date_data_per_hour(name_of_coin,
                                                      time.ctime(my_t),
                                                      list_of_points[my_time]["v"][0]))
    return history_of_coin


def main():
    """Главная функция вызывающая все остальные"""
    files = os.listdir(PATH_OF_PER_HOUR)
    write_into_csv.create()
    for file in files:
        js, name_of_coin = get_js_from_file(file)
        list_of_dates = get_all_data_per_hour(js, name_of_coin)
        write_into_csv.insert(list_of_dates)
        print(f"Файл {file} обработан!")
        # my_dbase.insert_list(list_of_dates)


if __name__ == "__main__":
    main()
