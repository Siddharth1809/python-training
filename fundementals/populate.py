from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:Mtech@localhost/sales")
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

c1 = Customers(name='abc', address='Hyd', email='abc@gmail.com')

session.add(c1)
session.commit()












