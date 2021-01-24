# -*- coding: utf-8 -*-
import os
if os.getenv("DEPLOY_ENV") == "prod":
    print("生产")
    from .prod import *
else:
    print("开发")
    from .dev import *
