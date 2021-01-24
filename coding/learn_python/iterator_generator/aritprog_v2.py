# -*- coding: UTF-8 -*-


def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index


if __name__ == '__main__':
    ap = aritprog_gen(0, 1, 3)
    print(list(ap))

    ap = aritprog_gen(1, .5, 3)
    print(list(ap))

    ap = aritprog_gen(0, 1/3, 1)
    print(list(ap))

    from fractions import Fraction
    ap = aritprog_gen(0, Fraction(1, 3), 1)
    print(list(ap))

    from decimal import Decimal
    ap = aritprog_gen(0, Decimal('.1'), .3)
    print(list(ap))
