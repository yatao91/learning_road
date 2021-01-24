# -*- coding: utf-8 -*-
smtpserver = "smtp.qq.com"  # will be read by smtp fixture


def test_showhelo(smtp_connection):
    assert 0, smtp_connection.helo()