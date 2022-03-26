import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import user, password, host, db_name
from my_schemas import base

DB_STR = f"postgresql+psycopg2://{user}:{password}@{host}/{db_name}"

db = create_engine(DB_STR)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)


def insert_list(datas):
    """Вставляем список"""
    update_time = str(datetime.datetime.now())[:10]
    for date in datas:
        c = Coins(coin_parse=date.coin_parse,
                  coin_time=date.coin_time,
                  coin_value=date.coin_value,
                  update_time=update_time)
        session.add(c)
    session.commit()


def insert_one(date):
    """Вставляем один элемент"""
    update_time = str(datetime.datetime.now())[:10]
    c = Coins(coin_parse=date.coin_parse,
              coin_time=date.coin_time,
              coin_value=date.coin_value,
              update_time=update_time)
    session.add(c)
    session.commit()
