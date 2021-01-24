# -*- coding: utf-8 -*-
"""
gevent调度器
"""
from datetime import datetime
import os

from apscheduler.schedulers.gevent import GeventScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = GeventScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    g = scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        g.join()
    except (KeyboardInterrupt, SystemExit):
        pass
