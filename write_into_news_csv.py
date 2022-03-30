import csv
import datetime


def create():
    """Создаем csv файл"""
    c1 = "news_parse"
    c2 = "news_time"
    c3 = "news_title"
    c4 = "news_lead"
    c5 = "update_time"
    with open(f"history_of_news.csv", "w+", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([c1, c2, c3, c4, c5])


def insert(list_of_news):
    """Добавляем новые строки в csv файл"""
    update_time = str(datetime.datetime.now())
    for news in list_of_news:
        with open(f"history_of_news.csv", "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([news.news_parse,
                             news.news_time,
                             news.news_title,
                             news.news_lead_p,
                             update_time])
