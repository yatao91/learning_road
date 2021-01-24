# -*- coding: utf-8 -*-
import threading
import random
import time


class Producer(threading.Thread):

    def __init__(self, integers, condition):
        threading.Thread.__init__(self)
        self.integers = integers
        self.condition = condition

    def run(self):
        while True:
            integer = random.randint(0, 256)
            self.condition.acquire()
            print("condition acquired by {}".format(self.name))

            self.integers.append(integer)
            print("{} appended to list by {}".format(integer, self.name))

            print("condition notified by {}".format(self.name))
            self.condition.notify()

            print("condition released by {}".format(self.name))
            self.condition.release()
            time.sleep(1)


class Consumer(threading.Thread):

    def __init__(self, integers, condition):
        threading.Thread.__init__(self)
        self.integers = integers
        self.condition = condition

    def run(self):
        while True:
            self.condition.acquire()
            print("condition acquired by {}".format(self.name))

            while True:
                if self.integers:
                    integer = self.integers.pop()
                    print("{} popped from list by {}".format(integer, self.name))
                    break
                print("condition wait by {}".format(self.name))
                self.condition.wait()

                print("condition released by {}".format(self.name))
                self.condition.release()


def main():
    integers = []
    condition = threading.Condition()
    t1 = Producer(integers, condition)
    t2 = Consumer(integers, condition)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()
