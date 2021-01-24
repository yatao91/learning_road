# -*- coding: utf-8 -*-
"""
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，
它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.dq = deque(maxlen=capacity)
        self.kv = dict()

    def get(self, key: int) -> int:
        if key in self.dq:
            self.dq.remove(key)
            self.dq.insert(0, key)
            return self.kv[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dq:
            self.dq.remove(key)
            self.dq.insert(0, key)
            self.kv[key] = value
        else:
            if len(self.dq) == self.dq.maxlen:
                remove_key = self.dq.pop()
                self.kv.pop(remove_key)
            self.dq.appendleft(key)
            self.kv[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == '__main__':
    dq = deque(maxlen=5)
    dq.append(1)
    dq.append(2)
    print(dq)
    index2 = dq.index(2)
    key = 2
    dq.remove(2)
    print(dq)
    dq.insert(0, key)
    print(dq)
    if 1 in dq:
        print('1')
    a = {"hardware": 1}
    a.pop("hardware")
    print(a)
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
