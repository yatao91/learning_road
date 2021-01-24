# -*- coding: utf-8 -*-
class Config(object):
    DEBUG = False


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
