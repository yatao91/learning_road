# -*- coding: UTF-8 -*-
import re


text = "测试_"

regex_str = r".*?([\u4E00-\u9FA5]+).*?"

match_obj = re.findall(regex_str, text)

if match_obj:
    print(match_obj)

if re.match(regex_str, text):
    print("match")
