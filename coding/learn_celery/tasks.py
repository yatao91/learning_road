# -*- coding: utf-8 -*-
from . import app


@app.task
def add(x, y):
    return x + y
