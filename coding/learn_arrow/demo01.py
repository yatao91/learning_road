# -*- coding: utf-8 -*-
import arrow

now = arrow.now()

now_str = now.strftime("%Y-%m-%d %H:%M:%S")
print(now_str)
