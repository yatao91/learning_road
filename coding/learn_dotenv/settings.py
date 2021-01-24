# -*- coding: utf-8 -*-
from dotenv import load_dotenv

load_dotenv()

import os

DEPLOY_ENV = os.getenv("DEPLOY_ENV", "local")
print(DEPLOY_ENV)
