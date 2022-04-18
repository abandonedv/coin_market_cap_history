import csv
import datetime


def create():
    """Создаем csv файл"""
    c1 = "news_parse"
    c2 = "news_time"
    c3 = "news_time_in_sec"
    c4 = "news_title"
    c5 = "news_lead"
    c6 = "update_time"
    with open(f"history_of_news.csv", "w+", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([c1, c2, c3, c4, c5, c6])


def insert(list_of_news):
    """Добавляем новые строки в csv файл"""
    update_time = str(datetime.datetime.now())

    with open(f"history_of_news.csv", "a", encoding="utf-8") as f:
        for news in list_of_news:
            writer = csv.writer(f)
            writer.writerow([news.news_parse,
                             news.news_time,
                             news.news_time_in_sec,
                             news.news_title,
                             news.news_lead_p,
                             update_time])
