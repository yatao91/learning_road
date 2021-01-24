# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint("hardware", __name__)


@bp.route("/aa")
def a():
    pass
