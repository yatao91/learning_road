# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@192.168.0.111:3306/su_test?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config.update(
    CELERY_BROKER_URL="redis://192.168.0.111:6380",
    CELERY_RESULT_BACKEND="redis://192.168.0.111:6380"
)
db = SQLAlchemy(app)
celery = make_celery(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username


@celery.task()
def add_together(a, b):
    return a + b


@celery.task()
def get_user(user_id):
    user = User.query.filter(User.id == user_id).first()
    username = user.username
    return username
