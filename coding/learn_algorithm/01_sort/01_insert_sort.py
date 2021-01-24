# -*- coding: UTF-8 -*-
"""
排序01--插入排序
可以类比为扑克牌游戏: 右手抓牌,左手持牌,每次右手抓的牌都要放入左手且要有序. 左手的始终有序.
"""


def insert_sort(seq: list):
    """
    插入排序(从小到大)
    :param seq: 待排序序列
    """
    # 第一层遍历:相当于从无序的牌中拿出一张
    for j in range(1, len(seq)):
        # 赋值给key作为待插入有序组的牌
        key = seq[j]
        # 有序组的最大牌的索引下标
        i = j - 1
        # 第二层循环:比较有序组中每张牌,若比待插入牌大,则进行移动
        while i >= 0 and seq[i] > key:
            # 将大牌往右移动
            seq[i + 1] = seq[i]
            i = i - 1
        # 将待插入牌插入到移动出的位置中
        seq[i + 1] = key


def insert_sort_desc(seq: list):
    """
    插入排序(从大到小)
    :param seq: 待排序序列
    """
    # 第一层遍历:相当于从无序的牌中拿出一张
    for j in range(1, len(seq)):
        # 赋值给key作为待插入有序组的牌
        key = seq[j]
        # 有序组的最大牌的索引下标
        i = j - 1
        # 第二层循环:比较有序组中每张牌,若比待插入牌大,则进行移动
        while i >= 0 and seq[i] < key:
            # 将大牌往右移动
            seq[i + 1] = seq[i]
            i = i - 1
        # 将待插入牌插入到移动出的位置中
        seq[i + 1] = key


if __name__ == '__main__':
    a = [4, 5, 8, 7, 2, 3, 6]
    insert_sort_desc(a)
    print(a)
