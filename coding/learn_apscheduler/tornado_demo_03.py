# -*- coding: utf-8 -*-
"""
tornado调度器
"""
import os
from datetime import datetime

from apscheduler.schedulers.tornado import TornadoScheduler
from tornado.ioloop import IOLoop


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = TornadoScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    g = scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        IOLoop.instance().start()
    except (KeyboardInterrupt, SystemExit):
        pass
