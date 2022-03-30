import datetime

from sqlalchemy import create_engine, select, desc
from sqlalchemy.orm import sessionmaker

from config import user, password, host, db_name
from my_schemas import base, Date, News

DB_STR = f"postgresql+psycopg2://{user}:{password}@{host}/{db_name}"

db = create_engine(DB_STR)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)


def insert_coin_list(datas):
    """Вставляем список"""
    update_time = str(datetime.datetime.now())[:10]
    for date in datas:
        c = Date(coin_parse=date.coin_parse,
                 coin_time=date.coin_time,
                 coin_value=date.coin_value,
                 update_time=update_time)
        session.add(c)
    session.commit()


def insert_one_coin(date):
    """Вставляем один элемент"""
    update_time = str(datetime.datetime.now())[:10]
    c = Date(coin_parse=date.coin_parse,
             coin_time=date.coin_time,
             coin_value=date.coin_value,
             update_time=update_time)
    session.add(c)
    session.commit()


def insert_news_list(news_list):
    """Вставляем список"""
    update_time = str(datetime.datetime.now())[:10]
    for news in news_list:
        c = News(news_parse=news.news_parse,
                 news_time=news.news_time,
                 news_title=news.news_title,
                 news_lead=news.news_lead_p,
                 update_time=update_time)
        session.add(c)
    session.commit()


def my_len():
    """Узнать число элементов"""
    return session.query(News).order_by(News.id.desc()).first().id


def get_all_by_time():
    """Получить все элементы БД отсортированные по времени"""
    return session.query(News).order_by(News.news_time).all()
