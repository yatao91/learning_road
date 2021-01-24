# -*- coding: utf-8 -*-
import logging

# filemode:指定日志文件写入方式 默认：追加 w：覆盖写
logging.basicConfig(filename='demo2.log', level=logging.DEBUG, filemode='w')
logging.debug('this message should go to the log file')
logging.info('so should this')
logging.warning('and this, too')
