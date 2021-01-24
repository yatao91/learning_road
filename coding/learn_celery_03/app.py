# -*- coding: utf-8 -*-
import time
from celery import Celery


celery_app = Celery('test',
                    broker='amqp://admin:admin@192.168.33.20:5672/')


@celery_app.task(bind=True, task_acks_late=True, task_reject_on_worker_lost=True)
def add(self, x, y):
    print(self.task_acks_late)
    print(self.task_reject_on_worker_lost)
    print('start')
    time.sleep(30)
    print('stop')
    return x + y
