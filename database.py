from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

link="mysql+mysqlconnector://root:swain%4012345@localhost:3306/product_db"
engine=create_engine(link)
session=sessionmaker(bind=engine,autoflush=True)
base=declarative_base()