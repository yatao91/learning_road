# -*- coding: utf-8 -*-
import threading
import time
import schedule


def job():
    print("runing on thread {}".format(threading.current_thread()))


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


schedule.every(5).seconds.do(run_threaded, job)
schedule.every(5).seconds.do(run_threaded, job)
schedule.every(5).seconds.do(run_threaded, job)
schedule.every(5).seconds.do(run_threaded, job)
schedule.every(5).seconds.do(run_threaded, job)


while 1:
    schedule.run_pending()
    time.sleep(1)
