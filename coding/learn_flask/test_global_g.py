# -*- coding: utf-8 -*-
from flask import Flask, g

app = Flask(__name__)


def get_attr(app):
    with app.app_context():
        if 'hardware' not in g:
            g.a = 'test'
    print(g.a)
    return g.a

get_attr(app)
