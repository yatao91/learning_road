# -*- coding: utf-8 -*-
from gevent.pywsgi import WSGIServer


def application(environ, start_response):
    status = '200 OK'

    headers = [
        ('Content-Type', 'text/html')
    ]

    start_response(status, headers)
    yield "<p>Hello"
    yield "World</p>"


WSGIServer(('127.0.0.1', 8000), application).serve_forever()
