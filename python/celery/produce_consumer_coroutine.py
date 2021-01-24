# -*- coding: utf-8 -*-
"""
子程序就是协程的一种特例

return的确是跳出函数，这是为consumer生成器提供了另一种终止方式c.send(None)。

当生成器第一次调用c.send(None)时，作用是预激，即启动生成器，效果等同于next(c)，
consumer函数执行到yield r后停止，生成第一个值''，只有在生成器启动之后，调用send方法才会赋值给n；

当生成器第二次及以后调用c.send(None)时，作用是终止生成器，效果等同于c.close()，
但有所不同的是，c.send(None)会抛出StopIteration异常，且异常中包含返回值，而c.close()方法则不会抛出异常。
"""


def consumer():
    r = ''
    while True:
        n = yield r  # consumer通过yield取消息, 同时通过yield把结果传回生产者
        if not n:
            print('test')
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)  # 启动生成器(consumer)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)  # 切换到生成器(consumer)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()  # produce不生产了, 关闭consumer


c = consumer()
produce(c)
