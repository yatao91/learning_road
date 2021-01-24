# -*- coding: utf-8 -*-
from celery import Celery


app = Celery("demo", broker='redis://127.0.0.1:6379/4', backend='redis://127.0.0.1:6379/5')
