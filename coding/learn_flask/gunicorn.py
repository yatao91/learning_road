# -*- coding: utf-8 -*-
workers = 1

threads = 1

bind = '0.0.0.0:8000'

pidfile = 'gunicorn.pid'

loglevel = 'info'

access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(hardware)s"'

accesslog = 'access.log'

errorlog = 'error.log'
