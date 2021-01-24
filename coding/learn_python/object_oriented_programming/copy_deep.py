# -*- coding: UTF-8 -*-
import copy
import functools


@functools.total_ordering
class MyClass:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name


a = MyClass('hardware')
my_list = [a]
dup = copy.deepcopy(my_list)

print(id(my_list), id(dup))
print('             my_list:', my_list)
print('                 dup:', dup)
print('      dup is my_list:', (dup is my_list))  # False
print('      dup == my_list:', (dup == my_list))  # True
print('dup[0] is my_list[0]:', (dup[0] is my_list[0]))  # True
print('dup[0] == my_list[0]:', (dup[0] == my_list[0]))  # True
