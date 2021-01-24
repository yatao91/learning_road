# -*- coding: utf-8 -*-
from flask import Blueprint

bp_a = Blueprint("hardware", __name__, url_prefix="/hardware")


@bp_a.route("/")
def index():
    return "Index Page"


@bp_a.route("/hello", methods=["GET", "POST"])
def hello():
    return "Hello hardware"
