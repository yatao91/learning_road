# -*- coding: utf-8 -*-
import schedule
import time
import threading

cease_continuous_run = threading.Event()


class ScheduleThread(threading.Thread):
    @classmethod
    def run(cls):
        while not cease_continuous_run.is_set():
            schedule.run_pending()
            time.sleep(1)


# 启动flask的时候同时启动该线程（定时任务队列轮询）
def start_task():
    continuous_thread = ScheduleThread()
    continuous_thread.start()


def job(work):
    print(work)


def add_job():
    schedule.every(5).seconds.do(job, 'suyatao').tag(str('suyatao'))

    return 'add success'


if __name__ == '__main__':
    add_job()
    start_task()
