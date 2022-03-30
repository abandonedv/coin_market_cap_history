import csv
import datetime


def create():
    """Создаем csv файл"""
    c1 = "coin_parse"
    c2 = "coin_time"
    c3 = "coin_value"
    c4 = "update_time"
    with open(f"history_of_coins.csv", "w+", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([c1, c2, c3, c4])


def insert(list_of_dates):
    """Добавляем новые строки в csv файл"""
    update_time = str(datetime.datetime.now())
    for date in list_of_dates:
        with open(f"history_of_coins.csv", "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([date.coin_parse,
                             date.coin_time,
                             date.coin_value,
                             update_time])
