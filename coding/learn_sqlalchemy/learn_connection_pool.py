# -*- coding: utf-8 -*-
import threading
import time

from sqlalchemy import create_engine

engine = create_engine(
    'mysql+pymysql://root:syt19910109@localhost/test?charset=utf8',
    encoding='utf8',
    echo=False,
    pool_size=10,
    pool_recycle=60
)


def order_by():
    sql = "SELECT COUNT(*) FROM `runoob_tbl`"
    engine.execute(sql)


def with_thread_test_pool_recyle():
    thread_list = []
    for _ in range(15):
        t = threading.Thread(target=order_by)
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()


def test_pool_recyle():
    while 1:
        print('thread start')
        with_thread_test_pool_recyle()
        print('thread end')
        time.sleep(60)


if __name__ == '__main__':
    test_pool_recyle()
