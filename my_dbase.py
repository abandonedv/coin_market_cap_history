import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from my_schemas import base, Date, News
from config import *


# psql -h localhost -p 5432 -U postgres -d Diplom

DB_STR = f"postgresql+psycopg2://{user}:{password}@{host}/{db_name}"

db = create_engine(DB_STR)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)


def insert_coin_list(datas):
    """Вставляем список"""
    update_time = str(datetime.datetime.now())
    for date in datas:
        c = Date(coin_parse=date.coin_parse,
                 coin_time=date.coin_time,
                 coin_time_in_sec=date.coin_time_in_sec,
                 coin_value=date.coin_value,
                 update_time=update_time)
        session.add(c)
    session.commit()


async def insert_one_coin(date):
    """Вставляем один элемент"""
    update_time = str(datetime.datetime.now())
    c = Date(coin_parse=date.coin_parse,
             coin_time=date.coin_time,
             coin_time_in_sec=date.coin_time_in_sec,
             coin_value=date.coin_value,
             update_time=update_time)
    session.add(c)
    session.commit()


def insert_news_list(news_list):
    """Вставляем список"""
    update_time = str(datetime.datetime.now())
    for news in news_list:
        c = News(news_parse=news.news_parse,
                 news_time=news.news_time,
                 news_title=news.news_title,
                 news_lead=news.news_lead_p,
                 update_time=update_time)
        session.add(c)
    session.commit()


def delete_coins(border):
    return session.query(Date).\
        filter(Date.coin_time_in_sec > 1648575540).\
        all()

def delete_coins1(border):
    session.query(Date).\
        filter(Date.coin_time_in_sec > 1648575540).\
        delete()
    session.commit()

def my_len_news():
    """Узнать число элементов"""
    return session.query(News) \
        .order_by(News.id.desc()) \
        .first() \
        .id


def my_len_coins():
    """Узнать число элементов"""
    return session.query(Date) \
        .order_by(Date.id.desc()) \
        .first() \
        .id


def get_all_news_by_time():
    """Получить все элементы БД отсортированные по времени"""
    return session.query(News) \
        .order_by(News.news_time) \
        .all()


def get_all_coin_hist_by_time(coin_name):
    """Получить все элементы БД отсортированные по времени"""
    return session.query(Date) \
        .filter(Date.coin_parse == coin_name) \
        .order_by(Date.coin_time) \
        .all()


def get_range_coin_hist_by_time(params):
    """Получить элементы в диапазоне из БД отсортированные по времени"""
    return session.query(Date) \
        .filter(Date.coin_parse == params.coin_name,
                Date.coin_time >= params.time_begin,
                Date.coin_time <= params.time_end) \
        .order_by(Date.coin_time) \
        .all()


def get_range_news_hist_by_time(params):
    """Получить элементы в диапазоне из БД отсортированные по времени"""
    return session.query(News) \
        .filter(News.news_time >= params.time_begin,
                News.news_time <= params.time_end) \
        .order_by(News.news_time) \
        .all()


def get_page_coin_hist_by_time(params):
    """Получить элементы по номеру страницы из БД отсортированные по времени"""
    return session.query(Date) \
               .filter(Date.coin_parse == params.coin_name) \
               .order_by(Date.coin_time.desc()) \
               .all()[params.page * params.n_rows - params.n_rows:params.page * params.n_rows]


def get_page_news_hist_by_time(params):
    """Получить элементы по номеру страницы из БД отсортированные по времени"""
    return session.query(News) \
               .order_by(News.news_time.desc()) \
               .all()[params.page * params.n_rows - params.n_rows:params.page * params.n_rows]


def get_all_coin_names():
    return session.query(Date) \
        .order_by(Date.coin_time.desc()) \
        .limit(20) \
        .all()


def get_time_of_last_update_of_coin(coin_name):
    """Узнать число элементов"""
    return session.query(Date) \
        .filter(Date.coin_parse == coin_name) \
        .order_by(Date.coin_time.desc()) \
        .first() \
        .coin_time


def get_time_of_last_news():
    """Узнать число элементов"""
    return session.query(News) \
        .order_by(News.news_time.desc()) \
        .first()

mmy_list = delete_coins("fv")
print(mmy_list)