# -*- coding: UTF-8 -*-
# 1.abs():返回数字的绝对值(整数或浮点数)
a = -1
a_abs = abs(a)
print(a_abs)

# 2.all(iterable):可迭代对象的每个元素均为真时返回真
a = [1, 2, 3]
if all(a):
    print(1)

b = [1, False, 3]
if all(b):
    print(1)
else:
    print(2)

# 3.any(iterable):可迭代对象的任意一个元素为真时返回真
a = [1, 0, 0]
if any(a):
    print(1)

b = [False, 0, 0]
if any(b):
    print(1)
else:
    print(2)

# ascii(object):类似repr(),打印一个对象的可打印的字符形式
a = "abc"
print(ascii(a))
print(repr(a))

# bin(x):将一个整数转换为"0b"开头的二进制字符串. 如果x不是整数int,它必须实现__index__()方法返回一个整型
a = 3
print(bin(a))
b = -10
print(bin(-10))


class LikeInt:

    def __index__(self):
        return -10


c = LikeInt()
print(bin(c))

# class bool([x]):返回布尔值:True or False 如果x为False或省略,返回False. 其他返回True.
# bool类是int的子类.不能够继续子类化
a = 1
print(bool(a))
print(bool())

"""
class bytearray([source[,encoding[,errors]]]): 返回一个bytes数组.
bytearray类是一个可变整数序列,整数范围:0<= x < 256
和可变序列一样拥有通用的方法 而且和bytes的大多数方法一致
可选的source参数可以用来实例化array用以下几种方式:
1.source--string, 必须提供encoding参数和可选的errors参数.bytearray()将string转换为bytes用str.encode()
2.source--integer, array将有source大小, 将使用null bytes进行实例化
3.source--object--符合buffer接口的对象,一个只读的缓冲区对象将用来实例化bytes array
4.source--iterable,如果是可迭代对象,则必须是一个整数范围在0-256的整型可迭代对象, 用来array的初始化内容

不传参的情况下, 一个size为0的array被创建
"""
a = bytearray()
print(a)
b = bytearray(source="sss", encoding="utf-8")
print(b)
c = bytearray([1, 2, 3])
print(c)

"""
class bytes([source[,encoding],errors]]]): 返回一个新的bytes对象
bytes类是一个不可变整数序列,整数范围:0<= x < 256
bytes是bytearray的不可变版本
"""

"""
callable(object):如果object可以调用,返回True;否则False
如果返回为True,调用仍然可能失败;但如果返回False,调用必定失败.
类是可调用的,调用一个类,返回一个新实例
如果类有__call__()方法,则实例是可调用的
"""
class DemoClass:

    def __call__(self, *args, **kwargs):
        print("callable")

print(callable(DemoClass))
DemoClass()()
print(callable(DemoClass()))


















