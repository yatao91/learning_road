# -*- coding: utf-8 -*-
from time import sleep

import rpyc


conn = rpyc.connect('localhost', 12345)
job = conn.root.add_job('server:print_text', 'interval', args=['Hello,world'], seconds=2)
sleep(10)
conn.root.remove_job(job.id)
