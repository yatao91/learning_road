# -*- coding: utf-8 -*-
from flask import url_for

from app import create_app

app = create_app()


if __name__ == '__main__':
    with app.test_request_context():
        print(url_for("hardware.hello"))
    app.run(debug=True)
