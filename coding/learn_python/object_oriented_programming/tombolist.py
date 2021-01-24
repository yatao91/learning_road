# -*- coding: UTF-8 -*-
from random import randrange

from tombola import Tombola


@Tombola.register
class TomboList(list):

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


# Python3.3之前需要使用这种方式
# Tombola.register(TomboList)
