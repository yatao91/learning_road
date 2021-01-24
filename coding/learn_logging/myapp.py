# -*- coding: utf-8 -*-
import logging
import mylib


def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info("started")
    mylib.do_something()
    logging.info("finished")


if __name__ == '__main__':
    main()
