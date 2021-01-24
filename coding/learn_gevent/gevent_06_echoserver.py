# -*- coding: utf-8 -*-
from __future__ import print_function
from gevent.server import StreamServer


def echo(socket, address):
    print("New connection from %s:%s" % address)
    socket.sendall(b"Welcome to the echo server! Type quit to exit.\r\n")

    rfileobj = socket.makefile(mode='rb')
    while True:
        line = rfileobj.readline()
        if not line:
            print("client disconnectted")
            break
        if line.strip().lower() == b'quit':
            print("client quit")
            break
        socket.sendall(line)
        print("echoed %r" % line)
    rfileobj.close()


if __name__ == '__main__':
    server = StreamServer(('127.0.0.1', 16000), echo)
    print("Starting echo server on port 16000")
    server.serve_forever()
