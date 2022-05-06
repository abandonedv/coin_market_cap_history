import pprint
import json
import os
import time
from time_data import time_data
from my_classes import DateData
import write_into_coin_csv
import my_dbase
from time_const import *

PATH_OF_PER_DAY = "saved_json_per_day"
PATH_OF_PER_HOUR = "C:\\Users\\Vadim\\Documents\\GitHub\\saved_json_per_hour"


def get_json_from_file(file):
    """Извлекаем json объект из json файла"""
    with open(PATH_OF_PER_HOUR + "/" + file, 'r') as f:
        my_json = json.load(f)
        name = file.split("_")[0]
        return my_json, name


def get_all_data_per_day(my_json):
    """Создаем список объектов date_data"""
    history_of_coin = []
    list_of_quotes = my_json["data"]["quotes"]
    name_of_coin = my_json["data"]["name"]
    for day_data in list_of_quotes:
        # pprint.pprint(day_data)
        history_of_coin.append(Date_data(name_of_coin,
                                         day_data["timeClose"][:10],
                                         day_data["quote"]["close"]))
    return history_of_coin


def get_all_data_per_hour(my_json, name_of_coin):
    """Создаем список объектов date_data"""
    history_of_coin = []
    list_of_points = my_json["data"]["points"]
    last_time = 0
    for my_time in list_of_points:
        my_t = int(my_time)
        if last_time + HOUR <= my_t:
            last_time = my_t
            # pprint.pprint(day_data)
            history_of_coin.append(DateData(name_of_coin,
                                            time_data(time.ctime(my_t), time_need=True),
                                            my_t,
                                            list_of_points[my_time]["v"][0]))
    return history_of_coin


def main_insert():
    files = os.listdir(PATH_OF_PER_HOUR)
    print(
        "1 - csv\n"
        "2 - db\n"
        "3 - 1 & 2\n"
    )
    type_of_use = int(input("Your type: "))
    if type_of_use == 1 or type_of_use == 3:
        write_into_coin_csv.create()
    for file in files:
        my_json, name_of_coin = get_json_from_file(file)
        list_of_dates = get_all_data_per_hour(my_json, name_of_coin)
        if type_of_use == 1 or type_of_use == 3:
            write_into_coin_csv.insert(list_of_dates)
        if type_of_use == 2 or type_of_use == 3:
            my_dbase.insert_coin_list(list_of_dates)
        print(f"Файл {file} обработан!")


def main():
    """Главная функция вызывающая все остальные"""
    main_insert()


if __name__ == "__main__":
    main()
