# -*- coding: utf-8 -*-
"""
LRU缓存--用于关键词搜索部分缓存
1.缓存池大小:10万
2.增量更新后刷新缓存池缓存
涉及对应key
1.zhongzhao:cache:lru:counter---缓存池大小--string
2.zhongzhao:cache:keyword:{keyword_md5}---某关键词缓存key--hash
    key:关键词
    value:关键词对应结果(es搜索原始结果)
    next:下一缓存key
    prev:前一缓存key
3.zhongzhao:cache:lru:head---头结点--hash
    key:0
    value:0
    next:最新缓存key
    prev:None
4.zhongzhao:cache:lru:tail---尾结点--hash
    key:0
    value:0
    next:None
    prev:最旧缓存key
"""
import json
import hashlib
from redis import StrictRedis

redis = StrictRedis(host="192.168.0.111",
                    port=6380,
                    db=13,
                    decode_responses=True)


LRU_CAPACITY = 3
LRU_HEAD_KEY = "zhongzhao:cache:lru:head"
LRU_TAIL_KEY = "zhongzhao:cache:lru:tail"
LRU_KEY_FORMAT = "zhongzhao:cache:keyword:{}"
LRU_COUNTER_KEY = "zhongzhao:cache:lru:counter"


class DLinkedNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def to_dict(self):
        node_dict = {"key": self.key,
                     "value": self.value if isinstance(self.value, str) else json.dumps(self.value),
                     "prev": self.prev,
                     "next": self.next}
        return node_dict


class LRUCache:

    def __init__(self, cache):
        self.capacity = LRU_CAPACITY
        self.cache = cache
        self.size = self._get_counter(LRU_COUNTER_KEY)
        self.head = self._get_node(LRU_HEAD_KEY)
        self.tail = self._get_node(LRU_TAIL_KEY)

    def _get_counter(self, key):
        counter = int(self.cache.get(key))
        return counter

    def _get_node(self, key):
        node_dict = self.cache.hgetall(key)
        node = DLinkedNode(**node_dict)
        return node

    def _add_node(self, node):
        """
        添加结点
        :param node: 待添加结点
        :return:
        """
        # 将结点前驱指向head的key
        node.prev = self.head.key
        # 将结点后继指向之前head的后继结点
        node.next = self.head.next

        # 获取之前head结点的后继结点
        old_head_next_node = self._get_node(key=self.head.next)

        # 构造待添加结点的key
        node_key = LRU_KEY_FORMAT.format(hashlib.md5(node.key.encode("utf-8")).hexdigest())
        # 将原head后继结点的前驱结点置为待添加结点key
        old_head_next_node.prev = node_key
        # 将head后继结点置为待添加结点key
        self.head.next = node_key

        # 获取head结点内容
        head_node_dict = self.head.to_dict()
        # 获取原head结点的后继结点内容
        old_head_next_node_dict = old_head_next_node.to_dict()
        # 获取待添加结点内容
        new_node_dict = node.to_dict()

        # 获取head结点key/原head的后继结点key/待添加结点key
        head_node_key = LRU_HEAD_KEY
        old_head_next_node_key = old_head_next_node.key
        new_node_key = node.key

        # 需要判断原head后继结点是否是尾结点
        if old_head_next_node_key == LRU_TAIL_KEY:
            print("原后继结点是TAIL")
            old_head_next_key = LRU_TAIL_KEY
        else:
            print("原后继结点不是TAIL")
            old_head_next_key = LRU_KEY_FORMAT.format(hashlib.md5(old_head_next_node_key.encode("utf-8")).hexdigest())

        new_key = LRU_KEY_FORMAT.format(hashlib.md5(new_node_key.encode("utf-8")).hexdigest())

        self.cache.hmset(head_node_key, head_node_dict)
        self.cache.hmset(old_head_next_key, old_head_next_node_dict)
        self.cache.hmset(new_key, new_node_dict)

    def _remove_node(self, node):
        """
        移除某结点
            1.取出待移除结点的前驱结点和后继结点
            2.将待移除结点的前驱结点的后继指针指向待移除结点的后继结点
            3.将待移除结点的后继结点的前驱指针指向待移除结点的前驱结点
        :param node: 待移除结点
        :return:
        """
        # 获取待移除结点前驱和后继结点key
        prev_key = node.prev
        new_key = node.next

        # 获取前驱和和后继结点
        prev_node = self._get_node(key=prev_key)
        new_node = self._get_node(key=new_key)

        # 将前驱和后继结点进行关联
        prev_node.next = new_key
        new_node.prev = prev_key

        # 更新删除结点后的前驱后继结点
        prev_node_dict = prev_node.to_dict()
        new_node_dict = new_node.to_dict()

        # 获取前驱后继结点key(需判断是否是head和tail,然后做key组装)
        prev_node_key = prev_node.key
        if prev_node_key == LRU_HEAD_KEY:
            print("前驱结点是头结点")
            prev_key = LRU_HEAD_KEY
        else:
            print("前驱结点非头结点")
            prev_key = LRU_KEY_FORMAT.format(hashlib.md5(prev_node_key.encode("utf-8")).hexdigest())
        new_node_key = new_node.key
        if new_node_key == LRU_TAIL_KEY:
            print("后继结点是尾结点")
            new_key = LRU_TAIL_KEY
        else:
            print("后继结点非尾结点")
            new_key = LRU_KEY_FORMAT.format(hashlib.md5(new_node_key.encode("utf-8")).hexdigest())

        # 更新前驱后继结点
        self.cache.hmset(prev_key, prev_node_dict)
        self.cache.hmset(new_key, new_node_dict)

    def _move_to_head(self, node):
        """
        将被访问或被更新的结点移向head
            1.先删除此结点
            2.添加此结点
        :param node: 被访问或被更新
        :return:
        """
        # 1.删除结点
        self._remove_node(node)
        # 2.添加此结点到head后
        self._add_node(node)

    def _pop_tail(self):
        """
        剔除最久未被使用结点
        :return:
        """
        # 获取最久未被使用结点key
        pop_key = self.tail.prev
        res_node = self._get_node(pop_key)
        self._remove_node(res_node)
        self.cache.delete(pop_key)

    def get(self, key):
        """
        获取某key缓存,并将此key置为最新
        :param key:
        :return:
        """
        key_md5 = LRU_KEY_FORMAT.format(hashlib.md5(key.encode("utf-8")).hexdigest())
        data = self.cache.hgetall(key_md5)
        # 未获取到数据
        if not data:
            # 返回None
            return None
        # 获取到数据,使用数据获取结点
        node = DLinkedNode(**data)
        # 将此结点移向头部
        self._move_to_head(node)
        value = json.loads(data['value'])
        return value

    def put(self, key, value):
        node_key = LRU_KEY_FORMAT.format(hashlib.md5(key.encode("utf-8")).hexdigest())
        # 尝试获取缓存
        data = self.cache.hgetall(node_key)
        # 判存
        if data:
            # 存在,构造结点
            node = DLinkedNode(**data)
        else:
            # 不存在,结点置空
            node = None

        # 如果结点不存在,进行增加结点操作
        if not node:
            print("结点不存在, 进行增加结点操作")
            # 构造孤立结点
            newNode = DLinkedNode(key=key, value=value)

            # 将孤立结点增加进链表
            self._add_node(newNode)
            self.size += 1
            self.cache.incr(LRU_COUNTER_KEY)

            # 增加新结点后,超出LRU容量,则进行剔除队尾结点操作
            if self.size > self.capacity:
                print("LRU容量超出,进行剔除最久未使用key")
                self._pop_tail()
                self.size -= 1
                self.cache.decr(LRU_COUNTER_KEY)
        else:
            node.value = value
            self._move_to_head(node)


if __name__ == '__main__':
    lru_cache = LRUCache(cache=redis)
    # lru_cache.put(key="关键词04", value=["04"])
    data = lru_cache.get(key="关键词02")
    print(data)
