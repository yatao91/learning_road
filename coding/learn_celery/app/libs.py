# -*- coding: utf-8 -*-
from redis import StrictRedis

redis = StrictRedis(host='127.0.0.1', port='6380', db=3, decode_responses=True)
