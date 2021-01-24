# -*- coding: utf-8 -*-
import asyncio
import aioredis


async def connect_uri():
    conn = await aioredis.create_connection(
        'redis://localhost/0')
    val = await conn.execute('GET', 'my-key')


async def connect_tcp():
    conn = await aioredis.create_connection(
        ('localhost', 6379))
    val = await conn.execute('GET', 'my-key')


async def connect_unixsocket():
    conn = await aioredis.create_connection(
        '/path/to/redis/socket')
    # or uri 'unix:///path/to/redis/socket?db=1'
    val = await conn.execute('GET', 'my-key')


asyncio.get_event_loop().run_until_complete(connect_tcp())
asyncio.get_event_loop().run_until_complete(connect_unixsocket())
