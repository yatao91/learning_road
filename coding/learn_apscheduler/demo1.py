# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', second=3)
scheduler.start()
