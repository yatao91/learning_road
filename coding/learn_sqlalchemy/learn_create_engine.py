# -*- coding: utf-8 -*-
import time

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String


# 引擎---一个进程中存在一个实例即可
engine = create_engine("mysql+mysqlconnector://root:123456@192.168.138.191/hou_test",
                       pool_size=4, max_overflow=0, pool_pre_ping=True)

conn1 = engine.connect()
conn2 = engine.connect()
conn3 = engine.connect()
conn4 = engine.connect()
# conn5 = engine.connect()
print(111)
time.sleep(30)

# 连接---每次使用时建立连接
conn = engine.connect()

result = conn.execute("SELECT `project` FROM `project`")
for row in result:
    print("project:", row['project'])

# 关闭连接---使用完毕关闭连接
conn.close()

# 直接使用engine进行查询---连接会自动释放返回连接池
result = engine.execute("SELECT `project` FROM `project`")
print(type(result), result, result.__dict__)
for row in result:
    print("project:", row['project'])
