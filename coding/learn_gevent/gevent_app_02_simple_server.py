# -*- coding: utf-8 -*-
from gevent.server import StreamServer


def handle(socket, address):
    socket.send(b"Hello from hardware telnet!\n")
    for i in range(5):
        socket.send(bytes(str(i) + '\n', encoding="utf-8"))
    socket.close()


server = StreamServer(('127.0.0.1', 5000), handle)
server.serve_forever()
