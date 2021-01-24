# -*- coding: utf-8 -*-
"""
author:      苏亚涛
email:       yataosu@gmail.com
create_time: 2019/10/25 11:29
file:        m2m_insert.py
ide:         PyCharm
"""
from coding.learn_sqlalchemy import m2m
from sqlalchemy.orm import sessionmaker

session_class = sessionmaker(bind=m2m.engine)
session = session_class()

a1 = m2m.Author(name="sbhong")

books = session.query(m2m.Book).filter(m2m.Book.id == 1).one()

a1.books = [books]

session.add_all([a1])

session.commit()
