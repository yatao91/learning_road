# -*- coding: utf-8 -*-
import asyncio


async def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1)
    r = await asyncio.sleep(1)  # asyncio.sleep()也是一个coroutine,所以线程不会等待,而是直接中断执行下一个消息循环
    print("Hello again!")


# 获取eventloop
loop = asyncio.get_event_loop()

# 执行coroutine
loop.run_until_complete(hello())
loop.close()
