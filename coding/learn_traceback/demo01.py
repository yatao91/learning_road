# -*- coding: utf-8 -*-
import sys
import traceback
import logging

logger = logging.getLogger('traceback_test')


def func1():
    raise Exception("--func1 exception--")


def func2():
    func1()


def main():
    try:
        func2()
    except Exception as e:
        exc_type, exc_value, exc_traceback_obj = sys.exc_info()
        # print('exc_type: {}'.format(exc_type))
        # print('exc_value: {}'.format(exc_value))
        # print('exc_traceback_obj: {}'.format(exc_traceback_obj))
        # traceback.print_tb(tb=exc_traceback_obj)
        # traceback.print_exception(exc_type, exc_value, exc_traceback_obj, limit=2, file=sys.stdout)
        # traceback.print_exc(file=sys.stdout)
        logger.error(traceback.format_exc())


if __name__ == '__main__':
    main()
