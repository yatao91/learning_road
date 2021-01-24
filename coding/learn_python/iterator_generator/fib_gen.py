# -*- coding: UTF-8 -*-


def fib():
    a, b = 0, 1
    while 1:
        yield b
        a, b = b, a + b


if __name__ == '__main__':
    fib_gen = fib()
    print(fib_gen)

    print(next(fib_gen))
    print(next(fib_gen))
    print(next(fib_gen))
    print(next(fib_gen))
