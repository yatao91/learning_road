# -*- coding: utf-8 -*-
from collections import OrderedDict


d = OrderedDict({"apple": 4, "banana": 3, "pear": 5, "orange": 7})
print(d)

d.move_to_end("apple")
print(d)
d.move_to_end("apple", last=True)
print(d)
d.move_to_end("apple", last=False)
print(d)
values = d.values()
print(values)
d['apple'] = 2
print(d)
d['new'] = 8
print(d)
item = d.popitem(last=True)
print(item)
item2 = d.popitem(last=False)
print(item2)


class LastUpdatedOrderedDict(OrderedDict):

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)


d2 = LastUpdatedOrderedDict({"hardware": 1, "b": 2, "c": 3})
d2['b'] = 5
print(d2)
