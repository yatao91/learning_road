# -*- coding: UTF-8 -*-
import random


class BingoCage:

    def __init__(self, items):
        # 接受可迭代对象,并在本地构建副本--防止列表参数的意外副作用
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage.')

    def __call__(self, *args, **kwargs):
        return self.pick()


if __name__ == '__main__':
    bingo = BingoCage(range(3))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))
