# -*- coding: utf-8 -*-
"""
author:      苏亚涛
email:       yataosu@gmail.com
create_time: 2019/10/25 11:26
file:        m2m.py
ide:         PyCharm
"""
from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, DATE, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import event

Base = declarative_base()

book_m2m_author = Table("book_m2m_author", Base.metadata,
                        Column("id", Integer, primary_key=True),
                        Column('books_id', Integer, ForeignKey("books.id")),
                        Column('authors_id', Integer, ForeignKey("authors.id")))


class Timestamp:
    """ORM模型通用时间字段"""
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)
    deleted_at = Column(DateTime, default=None, nullable=True)


@event.listens_for(Timestamp, 'before_update', propagate=True)
def timestamp_before_update(mapper, connection, target):
    target.updated_at = datetime.now()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)
    deleted_at = Column(DateTime, default=None, nullable=True)

    authors = relationship("Author", secondary=book_m2m_author, back_populates="books")

    def __repr__(self):
        return self.name


class Author(Base, Timestamp):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    books = relationship("Book", secondary=book_m2m_author, back_populates="authors")

    def __repr__(self):
        return self.name


engine = create_engine("mysql+pymysql://root:123456@192.168.0.111:3306/su_test", encoding="utf-8", echo=True)

Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)
