# -*- coding: utf-8 -*-
import time

from tornado.httpclient import AsyncHTTPClient


def handle_response(response):
    print('222')
    print(response.body)


def asynchronous_visit():
    http_client = AsyncHTTPClient()
    http_client.fetch('www.baidu.com', callback=handle_response)


if __name__ == '__main__':
    asynchronous_visit()
    print('111')
