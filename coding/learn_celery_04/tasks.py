# -*- coding: utf-8 -*-
import logging
import time

from celery import Celery
from celery.signals import worker_init
from kombu.transport import TRANSPORT_ALIASES

TRANSPORT_ALIASES['newredis'] = 'transport:Transport'

# celery = Celery('tasks', broker='redis://192.168.33.20:6379/0')
# celery = Celery('tasks', broker='amqp://admin:admin@192.168.33.20:5672/')
celery = Celery('tasks', broker='newredis://192.168.33.20:6379/0')

celery.conf.update(
    CELERYD_PREFETCH_MULTIPLIER=1,
    CELERY_IGNORE_RESULT=True
)


def restroe_all_unacknowledged_messages():
    conn = celery.connection(transport_options={'visibility_timeout': 0})
    qos = conn.channel().qos
    qos.restore_visible()
    print('Unacknowledged messages restored')


@worker_init.connect
def configure(sender=None, conf=None, **kwargs):
    restroe_all_unacknowledged_messages()


@celery.task(acks_late=True)
def longtask(n):
    logging.info('Starting long task %s', n)
    time.sleep(60)
