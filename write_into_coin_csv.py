import csv
import datetime


def create():
    """Создаем csv файл"""
    c1 = "coin_parse"
    c2 = "coin_time"
    c3 = "coin_time_in_sec"
    c4 = "coin_value"
    c5 = "update_time"
    with open(f"history_of_coins.csv", "w+", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([c1, c2, c3, c4, c5])


def insert(list_of_dates):
    """Добавляем новые строки в csv файл"""
    update_time = str(datetime.datetime.now())

    with open(f"history_of_coins.csv", "a", encoding="utf-8") as f:
        for date in list_of_dates:
            writer = csv.writer(f)
            writer.writerow([date.coin_parse,
                             date.coin_time,
                             date.coin_time_in_sec,
                             date.coin_value,
                             update_time])
