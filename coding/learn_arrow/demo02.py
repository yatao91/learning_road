# -*- coding: utf-8 -*-
import arrow
import dateutil

timestamp = 1574819943217
tz = "Asia/Shanghai"
time_arrow = arrow.get(timestamp / 1000)
print(dir(time_arrow))
print(time_arrow)
time_arrow_local = time_arrow.to(tz)
print(time_arrow_local)
time_from_timestamp = arrow.Arrow.fromtimestamp(1574819943)
print(time_from_timestamp)
time_str = time_arrow_local.strftime("%Y-%m-%d")
print(time_str, type(time_str))
now = arrow.now()
print(now, now.timestamp)
