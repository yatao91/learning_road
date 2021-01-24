# -*- coding: utf-8 -*-
from celery import Celery

from coding.learn_celery_config.config import REDIS_CONFIG

celery_app = Celery(broker="redis://{}:{}/{}".format(REDIS_CONFIG['host'], REDIS_CONFIG['port'], REDIS_CONFIG['db']))
