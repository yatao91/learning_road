# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint("b", __name__)


@bp.route("/bb")
def b():
    pass
