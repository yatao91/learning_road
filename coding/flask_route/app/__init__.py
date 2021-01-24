# -*- coding: utf-8 -*-
from flask import Flask

from flask_route.app.views.a import bp_a
from flask_route.app.views.b import bp_b


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_a)
    app.register_blueprint(bp_b)
    return app
