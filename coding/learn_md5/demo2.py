# -*- coding: utf-8 -*-
import hashlib

data = "中招"

md5_str = hashlib.md5(data.encode('gbk')).hexdigest()
print(md5_str)
