# -*- coding: UTF-8 -*-
"""
类作用:通过向类构造方法中传入一些文本的字符串, 然后可以逐个单词迭代.
此类要实现序列协议, 这个类的对象可以迭代. 因为所有序列都可以迭代
通过索引从文本中提取单词
"""
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        # re.findall函数返回一个字符串列表,元素为正则表达式的全部非重叠元素
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        # 为了完善序列协议实现的__len__方法,为了让对象可迭代,没必要实现此方法
        return len(self.words)

    def __repr__(self):
        # reprlib.repr函数用于实现大型数据结构的简略字符串表示形式
        return 'Sentence(%s)' % reprlib.repr(self.text)


if __name__ == '__main__':
    s = Sentence('"The time has come, " the Walrus said,')
    print(s)
    for word in s:
        print(word)
    print(list(s))

    # 因为是序列,可以通过索引获取单词
    print(s[0], s[5])
