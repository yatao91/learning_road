# -*- coding: UTF-8 -*-


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        # 把变量标记为自由变量,即使在函数中为变量赋予新值了,也会变成自由变量. 如果为nonlocal声明的变量赋予新值,
        # 闭包中保存的绑定会更新
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


if __name__ == '__main__':
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
