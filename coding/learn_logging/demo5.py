# -*- coding: utf-8 -*-
import logging

logging.basicConfig(format='%(asctime)s %(message)s', datefmt="%m/%d/%Y %I:%M:%S %p")
logging.warning("is when this event was logged.")

# 获取日志记录器的好习惯：使用模块名
logger = logging.getLogger(__name__)
