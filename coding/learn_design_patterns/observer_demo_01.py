# -*- coding: utf-8 -*-
"""
观察者模式:定义了对象之间的一对多依赖, 当一个对象改变状态时, 它的所有观察者都会收到通知并自动更新.
"""
import itertools


class Publisher:

    def __init__(self):
        # 保存观察者对象
        self.observers = set()

    def add(self, observer, *observers):
        """添加观察者"""
        # 使用itertools.chain方法:支持接受一个或多个observer对象
        for observer in itertools.chain((observer,), observers):
            self.observers.add(observer)
            # 向此对象注册观察者时,执行观察者的update方法以使用模型当前状态初始化自己
            observer.update(self)

    def remove(self, observer):
        """移除观察者"""
        try:
            self.observers.discard(observer)
        except ValueError:
            print('Failed to remove: {}'.format(observer))

    def notify(self):
        """状态改变:通知观察者"""
        # 模型状态发生变化,调用notify方法,执行每个观察者的update方法,确保观察者反应模型的最新状态
        [observer.update(self) for observer in self.observers]


class DefaultFormatter(Publisher):

    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        # 返回发布者名+data值.type(self).__name__:获取类名,避免硬编码
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name, self._data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        """赋新值时进行转整数,并最后调用notify通知观察者更新状态"""
        try:
            self._data = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()


class HexFormatter:
    """观察者一"""
    def update(self, publisher):
        """接收模型通知后更新为模型最新状态"""
        print("{}: '{}' has now hex data= {}".format(type(self).__name__,
                                                     publisher.name, hex(publisher.data)))


class BinaryFormatter:
    """观察者二"""
    def update(self, publisher):
        print("{}: '{}' has now bin data= {}".format(type(self).__name__,
                                                     publisher.name, bin(publisher.data)))


def main():
    df = DefaultFormatter('test1')
    print(df)

    print()
    hf = HexFormatter()
    df.add(hf)
    df.data = 3
    print(df)

    print()
    bf = BinaryFormatter()
    df.add(bf)
    df.data = 21
    print(df)

    print()
    df.remove(hf)
    df.data = 40
    print(df)

    print()
    df.remove(hf)
    df.add(bf)

    df.data = 'hello'
    print(df)

    print()
    df.data = 4.2
    print(df)


if __name__ == '__main__':
    main()
