# -*- coding: utf-8 -*-
from flask import Flask

import gevent.monkey


# gevent.monkey.patch_all()


app = Flask(__name__)


@app.route('/')
def helloworld():
    return 'helloworld'


if __name__ == '__main__':
    app.run(debug=True)
