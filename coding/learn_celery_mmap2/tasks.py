# -*- coding: utf-8 -*-
from celery import Celery
import mmap
import contextlib

app = Celery(
    "tasks",
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/1",
)


@app.task()
def init_model():
    """加载训练模型"""
    with open('word.txt', encoding="utf-8") as f:
        with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
            while 1:
                pass


@app.task()
def training1():
    """训练"""
    with open('word.txt', encoding="utf-8") as f:
        with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
            content = m.read()
            print(content)
