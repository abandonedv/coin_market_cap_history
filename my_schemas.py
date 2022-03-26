from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class Dates(base):
    __tablename__ = 'coin_warehouse'
    id = Column(Integer, primary_key=True, autoincrement=True)
    coin_parse = Column(String)
    coin_time = Column(String)
    coin_value = Column(Float)
    update_time = Column(String)
