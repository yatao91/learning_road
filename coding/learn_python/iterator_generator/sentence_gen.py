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
        """生成器函数
        此方法是生成器函数,调用时会构建一个实现了迭代器接口的生成器对象,因此不用再定义SentenceIteration类了.
        """
        for word in self.words:
            yield word
        return  # 此return不是必须的.可以直接不写,直接返回None.不管有没有,都不会抛出StopIteration异常.


if __name__ == '__main__':
    s = Sentence('"The time has come, " the Walrus said,')
    print(s)
    for word in s:
        print(word)
    print(list(s))
