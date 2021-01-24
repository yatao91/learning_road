# -*- coding: utf-8 -*-
import time
from datetime import datetime

from schedule import Scheduler


def job(work):
    print(work, datetime.now())


def add_and_run_job(func, args):

    schedule = Scheduler()

    schedule.every(5).seconds.do(func, args)

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    add_and_run_job(job, "job1")
    time.sleep(1)
    add_and_run_job(job, "job2")
