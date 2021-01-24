# -*- coding: utf-8 -*-
"""
目的:将一个只读属性定义成一个property,并且在访问时才会计算结果;
但是一旦被访问后,希望结果被缓存起来,不用每次都去计算
为了提升性能
缺陷:此版本的计算出的值是可以被修改的.

"""
# 定义一个延迟属性的高效方法:使用一个描述器类


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        """只有当被访问属性不在实例底层的字典中时__get__()方法才会被触发,
        触发后计算一次并将属性计算的结果存储到实例的字典中"""
        if instance is None:
            return self
        else:
            value = self.func(instance)
            # 将属性值(func.__name__)放入实例的字典中,并使用的是属性相同的名字
            setattr(instance, self.func.__name__, value)
            return value


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')  # 仅出现一次
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')  # 仅出现一次
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    c = Circle(4.0)
    print(c.area)
    print(c.area)
    print(vars(c))
    print(c.perimeter)
    print(c.perimeter)
    print(vars(c))

    del c.area

    print(vars(c))

    print(c.area)
