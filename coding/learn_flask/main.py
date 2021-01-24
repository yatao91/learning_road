# -*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

from flask import Flask

from views.simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page, url_prefix='/simple_page')


@app.route('/')
def hello_world():
    app.logger.info('info log')
    app.logger.warning('warning log')
    app.logger.error('error log')
    return "Hello world"


if __name__ == '__main__':
    app.debug = True

    # 按照日志大小切分 maxBytes:日志大小 backupCount:保留的日志个数
    handler_file = RotatingFileHandler('flask_log', maxBytes=1024000, backupCount=10)

    # 按照日期进行切分 when="D":按天切分 backupCount:保留15天日志 encoding=UTF-8:使用utf8编码写日志
    handler_date = TimedRotatingFileHandler('flask_log', when='D', backupCount=15, encoding='UTF-8', delay=False, utc=True)

    # 记录日志到文件
    handler = logging.FileHandler('flask.log')

    # 实例化日志formatter
    formatter = logging.Formatter(fmt="[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s")

    # 添加日志格式化器到对应handler
    handler.setFormatter(formatter)

    # 添加handler到日志记录器
    app.logger.addHandler(handler)

    app.run()
