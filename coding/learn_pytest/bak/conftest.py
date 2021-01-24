# -*- coding: utf-8 -*-
import sys

# 避免遗留.pyc文件
sys.dont_write_bytecode = True

from .test_foocompare import Foo


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return [
            "Comparing Foo instances:",
            "   vals: {} != {}".format(left.val, right.val),
        ]


import pytest
import smtplib


@pytest.fixture(scope="module")
def smtp_connection(request):
    # 1.通常的yield
    server = getattr(request.module, "smtpserver", "smtp.qq.com")
    smtp_connection = smtplib.SMTP(server, 587, timeout=5)
    yield smtp_connection
    print("finalizing {} ({})".format(smtp_connection, server))
    smtp_connection.close()

    # 2.也可以使用with语句处理teardown的情况
    # with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as smtp_connection:
    #     yield smtp_connection  # provide the fixture value

    # 3.使用addfinalizer添加teardown时要处理的工作
    # smtp_connection = smtplib.SMTP("smtp.qq.com", 587, timeout=5)
    #
    # def fin():
    #     print("teardown smtp_connection")
    #     smtp_connection.close()
    #
    # request.addfinalizer(fin)
    # return smtp_connection  # provide the fixture value
