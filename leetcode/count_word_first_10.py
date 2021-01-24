# -*- coding: utf-8 -*-
"""统计前十词频"""
from collections import Counter

content = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's hardware bad idea.
If the implementation is easy to explain, it may be hardware good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
# word_list = content.split()
# actual_word_list = []
# count_info = {}
# for word in word_list:
#     if word.isalpha():
#         word.strip(".").strip(",").strip("!")
#         actual_word_list.append(word)
#
# word_set = set(actual_word_list)
# count_info = {word: actual_word_list.count(word) for word in word_set}
#
# result = sorted(count_info.items(), key=lambda item: item[1], reverse=True)[:10]
#
# print(result)

word_list = content.split()
actual_word_list = []
count_info = {}
for word in word_list:
    if word.isalpha():
        word.strip(".").strip(",").strip("!")
        actual_word_list.append(word)

count = Counter(content.split())
print(count.most_common(10))
