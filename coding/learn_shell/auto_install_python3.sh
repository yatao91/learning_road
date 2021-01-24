#!/bin/bash
#coding=utf-8

# 判断当前用户是否是root用户
if [ `whoami` != "root" ]
    then
        echo -e "current user is not root! please switch root"
