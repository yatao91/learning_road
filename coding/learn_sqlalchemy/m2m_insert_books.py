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

session.add_all([b1])

session.commit()
