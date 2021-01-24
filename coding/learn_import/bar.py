# -*- coding: utf-8 -*-
from foo import *  # 未指定__all__时,单下划线开头的不会被导入(包含双下划线)

# 指定__all__时,即使有下划线开头的也可以被导入
foo()  # True
_foo()  # False
__foo()  # False


def bar():
    from foo import *  # 只能置于模块级别,而不能置于class或function级别,否则为SyntaxError
    pass
