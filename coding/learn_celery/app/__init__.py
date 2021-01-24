# -*- coding: utf-8 -*-
from celery import Celery


app = Celery('test')

app.config_from_object('celery_app.config')
