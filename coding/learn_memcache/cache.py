# -*- coding: UTF-8 -*-
import memcache
import sys


addr = 'localhost'

len_argv = len(sys.argv)

if len_argv < 3:
    sys.exit("Not enough arguments")

port = sys.argv[1]

cache = memcache.Client(["{0}:{1}".format(addr, port)])

key = str(sys.argv[2])

if len_argv == 4:
    value = str(sys.argv[3])
    cache.set(key, value)
    print("Value for {0} set".format(key))
else:
    value = cache.get(key)
    print("Value for {0} is {1}".format(key, value))
