# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import current_app


simple_page = Blueprint('simple_page', __name__)


@simple_page.route('/')
def show():
    current_app.logger.info("simple page info log")
    current_app.logger.warning("simple page warning log")
    current_app.logger.error("simple page error log")
    return "simple page"
