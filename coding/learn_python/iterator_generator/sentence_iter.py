# -*- coding: UTF-8 -*-
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # 实现此方法: 表明此类可以迭代. 根据迭代器协议,__iter__方法实例并返回一个迭代器
        return SentenceIterator(self.words)


class SentenceIterator:

    def __init__(self, words):
        self.words = words  # 迭代器类引用单词列表
        self.index = 0  # index用于确定下一个要获取的单词

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


if __name__ == '__main__':
    s = Sentence('"The time has come, " the Walrus said,')
    print(s)
    for word in s:
        print(word)
    print(list(s))
