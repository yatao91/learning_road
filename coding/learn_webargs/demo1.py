# -*- coding: utf-8 -*-
from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args


app = Flask(__name__)

hello_args = {"name": fields.Str(required=True)}


@app.route('/', methods=['GET', 'POST'])
@use_args(hello_args)
def index(args):
    return "hello" + args['name']


if __name__ == '__main__':
    app.run(debug=True)
