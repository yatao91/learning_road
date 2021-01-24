import time
import threading

from flask import Flask


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args,
                                                                 **kwargs)
        return cls._instances[cls]


class Demo(object):

    def __init__(self, worker=None):
        self.worker = worker

    def run(self):
        if self.worker and self.worker.isAlive():
            return "ERROR: there's already a running cluster deployer"
        else:
            self.worker = Worker()
            self.worker.start()
            return "SUCCEEDED: A new cluster deploying task is on its way now."


class SingletonDemo(Demo):
    __metaclass__ = Singleton

    def __init__(self, *args, **kwargs):
        super(SingletonDemo, self).__init__(*args, **kwargs)


class Worker(threading.Thread):

    def run(self):
        print "worker task"


app = Flask(__name__)


@app.route("/hello")
def one():
    demo = SingletonDemo()
    resp = demo.run()
    print resp
    return resp


@app.route("/world")
def two():
    demo = SingletonDemo()
    resp = demo.run()
    print resp
    return resp


if __name__ == '__main__':
    app.run(threaded=True)
