# -*- coding: utf-8 -*-
from flask import Blueprint

bp_b = Blueprint("b", __name__, url_prefix="/b")


@bp_b.route("/hello")
def hello():
    return "Hello b"
