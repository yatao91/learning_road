# -*- coding: utf-8 -*-
import schedule
import time


def job(work):
    print(work)


schedule.every(10).seconds.do(job, "suyatao")

num = 0
while True:
    print(num)
    schedule.run_pending()
    time.sleep(1)
    num += 1
