import datetime

from sqlalchemy import create_engine, select, desc
from sqlalchemy.orm import sessionmaker

from config import user, password, host, db_name
from my_schemas import base, Date

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


def my_len():
    """Узнать число элементов"""
    return session.query(Date).order_by(Date.id.desc()).first().id

print(my_len())