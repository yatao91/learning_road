# -*- coding: utf-8 -*-
from array import array
import math


class Vector2d:
    # 类属性 在实例与字节序列之间转换时使用
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)  # 标记为私有属性
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        # 定义__iter__方法 变为可迭代对象,才能进行拆包
        return (i for i in (self.x, self.y))  # 通过self.x读取公开特性

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __repr__(self):
        # 因为实现了可迭代,所以*self会进行拆包给format函数
        class_name = type(self).__name__  # 为什么不硬编码类名:避免子类要覆盖__repr__方法
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        # 显示有序对
        return str(tuple(self))

    def __bytes__(self):
        # 为了生成字节序列
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        # 为了比较所有分量
        return tuple(self) == tuple(other)

    def __abs__(self):
        # 实现__abs__方法用于构成直角三角形斜边长
        return math.hypot(self.x, self.y)

    def angle(self):
        return math.atan2(self.y, self.x)

    def __bool__(self):
        return bool(abs(self))
    
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    @classmethod
    def frombytes(cls, octets):
        # 备选构造方法
        typecode = chr(octets[0])
        memv = memoryview(octets[1:].cast(typecode))
        return cls(*memv)
