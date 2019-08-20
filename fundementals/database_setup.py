import pymysql

from sqlalchemy import Column, String, Integer, ForeignKey

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine("mysql+pymysql://root:Mtech@localhost/books?charset=utf8mb4")

Base.metadata.create_all(engine)

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    genre = Column(String(250))


from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker(bind=engine)

session = DBSession()


bookOne = Book(title="The Bell Jar", author="Sylvia Pla", genre="roman à clef")
session.add(bookOne)
session.commit()