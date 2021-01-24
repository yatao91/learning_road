# -*- coding: utf-8 -*-
"""flask App 初始化"""
from flask import Flask
from werkzeug.utils import find_modules, import_string


def configure_blueprint(app):
    root = 'app.views'
    for name in find_modules(root, recursive=True, include_packages=True):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            project_name = name.rsplit(".")[-3]
            api_version = name.rsplit(".")[-2]
            model_name = name.rsplit(".")[-1]
            url_prefix = "/{}/{}/{}".format(project_name, api_version, model_name)
            app.register_blueprint(mod.bp, url_prefix=url_prefix)


def create_app():
    app = Flask(__name__)
    configure_blueprint(app)
    return app
