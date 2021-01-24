# -*- coding: utf-8 -*-
import re


def time_re(start_time, stop_time):
    if not re.match('^\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}$', start_time) \
            or not re.match('^\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}$', stop_time):
        print('error')


if __name__ == '__main__':
    start_time = '2019-05-15 15:38:38'
    stop_time = '2019-08-13 15:38:38'
    time_re(start_time, stop_time)
