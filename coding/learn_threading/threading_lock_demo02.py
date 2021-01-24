# -*- coding: utf-8 -*-
import threading


class Thread01(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global counter, lock
        if lock.acquire():
            for i in range(10):
                counter += 1
                print("thread:{} counter:{}".format(self.name, counter))
        lock.release()


class Thread02(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global counter, lock
        if lock.acquire():
            for i in range(10):
                counter += 10
                print("thread:{} counter:{}".format(self.name, counter))
        lock.release()


if __name__ == '__main__':
    counter = 0
    lock = threading.Lock()
    t1 = Thread01()
    t2 = Thread02()
    t1.start()
    t2.start()
