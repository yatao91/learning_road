# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@192.168.33.20:3306/test?charset=utf8'
app.config['SQLALCHEMY_POOL_SIZE'] = 5
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 10

db = SQLAlchemy()
db.init_app(app)


class Test(db.Model):
    __tablename__ = "test"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), nullable=True)

    @classmethod
    def get_test(cls, t_id):
        t = cls.query.filter(cls.id == t_id).first()
        return t.name


@app.teardown_request
def teardown_request(e):
    db.session.remove()


@app.route("/")
def hello():
    name = Test.get_test(t_id=1)
    print(name)
    return "hello world"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
