# -*- coding: UTF-8 -*-


class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        # 将self.begin的值赋值给result,不过先强制转换成前面的加法算式得到的类型.
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


if __name__ == '__main__':
    ap = ArithmeticProgression(0, 1, 3)
    print(list(ap))

    ap = ArithmeticProgression(1, .5, 3)
    print(list(ap))

    ap = ArithmeticProgression(0, 1/3, 1)
    print(list(ap))

    from fractions import Fraction
    ap = ArithmeticProgression(0, Fraction(1, 3), 1)
    print(list(ap))

    from decimal import Decimal
    ap = ArithmeticProgression(0, Decimal('.1'), .3)
    print(list(ap))
