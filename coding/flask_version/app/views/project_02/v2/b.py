# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint("c", __name__)


@bp.route("/bb", endpoint="test")
def c():
    pass
