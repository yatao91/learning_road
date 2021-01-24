# -*- coding: utf-8 -*-
"""
twisted调度器
"""
import os
from datetime import datetime

from apscheduler.schedulers.twisted import TwistedScheduler
from twisted.internet import reactor


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = TwistedScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    g = scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        reactor.run()
    except (KeyboardInterrupt, SystemExit):
        pass
