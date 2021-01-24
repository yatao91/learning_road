# -*- coding: UTF-8 -*-
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # finditer函数构建一个迭代器,包含self.text中匹配RE_WORD的单词,产出MatchObject实例
        for match in RE_WORD.finditer(self.text):
            # match.group()方法从MatchObject实例中提取匹配正则表达式的具体文本
            yield match.group()


if __name__ == '__main__':
    s = Sentence('"The time has come, " the Walrus said,')
    print(s)
    for word in s:
        print(word)
    print(list(s))
