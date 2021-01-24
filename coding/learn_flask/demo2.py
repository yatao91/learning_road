# -*- coding: utf-8 -*-
import logging

from flask import Flask


app = Flask(__name__)


@app.route('/')
def root():
    app.logger.info('info log')
    app.logger.warning('warning log')
    return 'hello'


if __name__ == '__main__':
    app.debug = True

    handler = logging.FileHandler('demo2.log', encoding='UTF-8')

    handler.setLevel(logging.DEBUG)

    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'
    )

    handler.setFormatter(logging_format)

    app.logger.addHandler(handler)

    app.run()
