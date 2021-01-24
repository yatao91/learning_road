# -*- coding: utf-8 -*-


def consumer():
    r = ''
    while True:
        # 拿到消息,并传回结果
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    # 启动生成器
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        # 切换到consumer执行
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    # 关闭consumer
    c.close()


if __name__ == '__main__':
    c = consumer()
    produce(c)
