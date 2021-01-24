# -*- coding: utf-8 -*-
from flask import Flask, current_app


def create_app():
    app = Flask(__name__)

    with app.app_context():
        config = current_app.config
        print(config)

    return app


app = create_app()
