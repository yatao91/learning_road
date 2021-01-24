# -*- coding: utf-8 -*-
from time import sleep
from tasks import longtask


for i in range(6):
    longtask.delay(i + 1)
    sleep(0.1)

