# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor


with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(pow, 4, 2)
    print(future.result())
