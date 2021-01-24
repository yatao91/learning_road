# -*- coding: utf-8 -*-
import threading
import gc

lock = threading.Lock()


class C(object):
    def __del__(self):
        print('getting lock')
        with lock:
            print('releasing lock')
            pass


# c = C()
# with lock:
#     # remove the variable c from the namespace
#     del c

# swap the final two statements
# c = C()
# del c
# with lock:
    # remove the variable c from the namespace
    # pass

c = C()
del c
with lock:
    # remove the variable c from the namespace
    gc.collect
