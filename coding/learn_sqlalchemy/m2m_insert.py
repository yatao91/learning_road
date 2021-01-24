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

b1 = m2m.Book(name="python", pub_date="2017-08-08")
b2 = m2m.Book(name="sb", pub_date="2017-10-08")
b3 = m2m.Book(name="zb", pub_date="2017-11-08")

a1 = m2m.Author(name="sbhong")
a2 = m2m.Author(name="sgaogao")
a3 = m2m.Author(name="dbhong")

b1.authors = [a1, a3]
b2.authors = [a1, a2, a3]

session.add_all([b1, b2, b3, a1, a2, a3])

session.commit()
