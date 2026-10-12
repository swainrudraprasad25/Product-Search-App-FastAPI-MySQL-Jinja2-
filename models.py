from sqlalchemy import Column, Integer, String

from database import base


class Product(base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    prod_name = Column(String(100))
    price = Column(Integer)
    company = Column(String(100))
