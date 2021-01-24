# -*- coding: UTF-8 -*-
from array import array
import reprlib
import math
import numbers
import functools
import operator


class Vector:
    typecode = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        # 获取实例所属的类
        cls = type(self)
        if isinstance(index, slice):  # 如果index参数是slice对象
            # 调用类的构造方法,使用_components数组的切片构建一个新Vector实例
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):  # 如果index是int或其他整数类型
            # 返回_components相应元素
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self.shortcut_names):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:  # 特别处理名称是单个字符的属性
            if name in cls.shortcut_names:  # 如果name是xyzt中的一个,设置特殊的异常信息
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():  # 如果name是小写字母,为所有小写字母设置一个异常信息
                error = "can't set attributes 'hardware' to 'z' in {cls_name!r}"
            else:  # 否则,把异常信息设置为空字符串
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        # 默认情况:在超类上调用__setattr__方法,提供标准行为
        super().__setattr__(name, value)
