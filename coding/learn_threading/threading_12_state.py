# -*- coding: utf-8 -*-
from socket import socket, AF_INET, SOCK_STREAM
import threading
from functools import partial


class LazyConnection:
    def __init__(self, address, family=AF_INET, sock_type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = sock_type
        self.local = threading.local()  # 使用线程本地存储对象来存储当前线程状态

    def __enter__(self):
        if hasattr(self.local, 'sock'):
            raise RuntimeError('Already connected')
        self.local.sock = socket(self.family, self.type)
        self.local.sock.connect(self.address)
        return self.local.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.local.sock.close()
        del self.local.sock


def demo(conn):
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.baidu.com\r\n')

        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))

    print('Got {} bytes'.format(len(resp)))


if __name__ == '__main__':
    conn = LazyConnection(address=('www.baidu.com', 80))

    t1 = threading.Thread(target=demo, args=(conn,))
    t2 = threading.Thread(target=demo, args=(conn,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
