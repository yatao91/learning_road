# -*- coding: UTF-8 -*-
import asyncio


async def nested():
    return 42


async def main():
    nested()
    print(await nested())


asyncio.run(main())
