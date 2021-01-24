# -*- coding: utf-8 -*-
import logging
from flask import Flask

logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route('/')
def index():
    logger.info("info log")
    logger.error("error log")
    return "Hello world!"


if __name__ != '__main__':
    # 如果不是直接运行，则将日志输出到 gunicorn 中
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
