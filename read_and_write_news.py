import pprint
import json
import os
import time
from my_classes import NewsData
import write_into_news_csv
import my_dbase
from time_data import time_data

PATH_OF_NEWS = "saved_json_tass"


def get_json_from_file(file):
    """Извлекаем json объект из json файла"""
    with open(PATH_OF_NEWS + "/" + file, 'r', encoding="utf-8") as f:
        my_json = json.load(f)
        return my_json


def get_all_news(my_json):
    """Создаем список объектов date_data"""
    history_of_news = []
    list_of_news = my_json["data"]["news"]
    for news_data in list_of_news:
        # pprint.pprint(day_data)
        data = NewsData(news_data)
        data.news_lead_p = news_data[0]
        history_of_news.append(data)
    return history_of_news


def main_insert():
    files = os.listdir(PATH_OF_NEWS)
    print(
        "1 - csv\n"
        "2 - db\n"
        "3 - 1 & 2\n"
    )
    type_of_use = int(input("Your type: "))
    if type_of_use == 1 or type_of_use == 3:
        write_into_news_csv.create()
    for file in files:
        my_json = get_json_from_file(file)
        list_of_news = get_all_news(my_json)
        if type_of_use == 1 or type_of_use == 3:
            write_into_news_csv.insert(list_of_news)
        if type_of_use == 2 or type_of_use == 3:
            my_dbase.insert_news_list(list_of_news)
        print(f"Файл {file} обработан!")


def main():
    """Главная функция вызывающая все остальные"""
    main_insert()


if __name__ == "__main__":
    main()
