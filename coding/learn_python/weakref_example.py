# -*- coding: utf-8 -*-
import weakref

_id2obj_dict = weakref.WeakKeyDictionary()


def remember(obj):
    oid = id(obj)
    _id2obj_dict[oid] = obj
    return oid


def id2obj(oid):
    return _id2obj_dict[oid]
