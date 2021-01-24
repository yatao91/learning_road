# -*- coding: utf-8 -*-


def spam():
    pass


def grok():
    pass


blah = 42

# 仅导出spam,grok.为空则不会导入任何.出现没有的内容会引发attributeerror
__all__ = []
