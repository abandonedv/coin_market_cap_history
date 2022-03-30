import pprint
import json
import os
import time

import write_into_news_csv

PATH_OF_NEWS = "saved_json_tass"


class News_data:
    def __init__(self, news):
        self.news_parse = news[0]["slug"]
        self.news_time = time.ctime(news[0]["publishDate"])
        self.news_title = news[0]["title"]
        self.__news_lead = "None"

    def get_news_lead(self):
        return self.__news_lead

    def set_news_lead(self, value):
        try:
            self.__news_lead = value["lead"]

        except:
            self.__news_lead = "None"

    news_lead_p = property(get_news_lead, set_news_lead)


def get_js_from_file(file):
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
        data = News_data(news_data)
        data.news_lead_p = news_data[0]
        history_of_news.append(data)
    return history_of_news


def main():
    """Главная функция вызывающая все остальные"""
    files = os.listdir(PATH_OF_NEWS)
    write_into_news_csv.create()
    for file in files:
        my_json = get_js_from_file(file)
        list_of_dates = get_all_news(my_json)
        write_into_news_csv.insert(list_of_dates)
        print(f"Файл {file} обработан!")
        # my_dbase.insert_list(list_of_dates)


if __name__ == "__main__":
    main()