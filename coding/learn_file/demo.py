# -*- coding: utf-8 -*-
# win10中文路径下,反斜杠可正常读写
filename = "d:/dev/projects/learning_road/coding/learn_file/文件/abc"

with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        print(line)
