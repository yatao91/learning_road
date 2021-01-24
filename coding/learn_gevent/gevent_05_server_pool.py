# -*- coding: utf-8 -*-
from gevent.server import StreamServer
from gevent.pool import Pool


def handle(socket, address):
    print('new connection!')


pool = Pool(10000)
server = StreamServer(('127.0.0.1', 1234), handle, spawn=pool)

server.serve_forever()
