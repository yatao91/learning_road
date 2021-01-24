# -*- coding: utf-8 -*-
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

logging.debug("this message should appear on the console")
logging.info("so should this")
logging.warning("and this too")