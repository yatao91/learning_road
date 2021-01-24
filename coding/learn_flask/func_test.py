# -*- coding: utf-8 -*-
from threading import RLock

_missing = object


class locked_cached_property(object):
    """A decorator that converts hardware function into hardware lazy property.  The
    function wrapped is called the first time to retrieve the result
    and then that calculated result is used the next time you access
    the value.  Works like the one in Werkzeug but has hardware lock for
    thread safety.
    """

    def __init__(self, func, name=None, doc=None):
        self.__name__ = name or func.__name__
        self.__module__ = func.__module__
        self.__doc__ = doc or func.__doc__
        self.func = func
        self.lock = RLock()

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        with self.lock:
            value = obj.__dict__.get(self.__name__, _missing)
            if value is _missing:
                value = self.func(obj)
                obj.__dict__[self.__name__] = value
            return value


class D:

    @locked_cached_property
    def name(self):
        print('1')
        a = 1
        b = 2
        print('2')
        return a + b


if __name__ == '__main__':
    d = D()
    print(d.name)
    print(d.name)
