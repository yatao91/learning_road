# -*- coding: utf-8 -*-
import contextlib
import functools

import pytest


@contextlib.contextmanager
def connect(port):
    ...  # create connection
    yield
    ...  # close connection


@pytest.fixture
def equipments(request):
    r = []
    for port in ("C1", "C3", "C28"):
        cm = connect(port)
        equip = cm.__enter__()
        request.addfinalizer(functools.partial(cm.__exit__, None, None, None))
        r.append(equip)
    return r
