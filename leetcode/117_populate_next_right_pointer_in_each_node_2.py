# -*- coding: utf-8 -*-
"""
二叉树:填充每个节点的下一个右侧节点指针2
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def processChild(self, childNode: 'Node', prev: 'Node', leftmost: 'Node') -> tuple:
        # 孩子节点存在
        if childNode:
            # prev指针已经设置,如果有至少一个节点在下一层则设置prev的next指针指向
            if prev:
                prev.next = childNode
            # prev指针不存在,则表示孩子节点为下一层的第一个节点,所以设置为下一层最左节点leftmost
            else:
                leftmost = childNode
            # prev指向当前孩子节点
            prev = childNode
        # 孩子节点不存在,则不对prev和leftmost进行更新
        return prev, leftmost

    def connect(self, root: 'Node') -> 'Node':
        """
        思路:使用已建立的next指针:第N层建立next指针后,再建立第N+1层节点的next指针
        1.leftmost:每层最左节点.每层最左节点作为链表首部,从该节点开始访问该层所有节点
        2.curr:用来遍历当前层的所有节点.从该层的最左节点一直移动到该层最后一个节点
        3.prev:指向下一层的节点.使用prev来指向下一层节点,来做next指针连接
            hardware.prev指针初始化.每层遍历开始时,prev指针置为空,找到下一层最左节点时,将该节点赋予prev指针
            b.当前节点没有左子节点时,将prev指向当前节点的右子节点
            c.下一个节点没有孩子节点,则不对prev指针进行更新
            d.下一个节点同时拥有左孩子和右孩子,首先prev指向左孩子,处理完后,指向右孩子.
        时间复杂度:O(n),每个节点均处理一次
        空间复杂度:O(1),不需要额外空间
        :param root: 原二叉树
        :return: 填充next指针后二叉树
        """
        if not root:
            return root

        # 第一层仅存在一个根节点,初始化最左节点为root节点
        leftmost = root

        # 循环遍历每一层,最左节点为空时退出循环.
        while leftmost:

            # 初始化每层prev和curr指针,prev指针初始化None,curr指针初始化为当前层最左节点,用来从该层首部通过next指针进行遍历
            prev, curr = None, leftmost

            # 初始化下一层最左节点leftmost为None
            leftmost = None

            # 根据next指针对当前层节点进行遍历
            while curr:
                # 处理当前节点的孩子节点并更新prev和leftmost指针
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)

                # 移动到当前层的下一个节点
                curr = curr.next

        return root

    def connect2(self, root: 'Node') -> 'Node':
        """
        思路:在当前层,把下一层的第一个节点用哨兵节点记录下来;然后遍历当前层的时候,把下面一层串起来(next指针),当前层遍历完,通过哨兵节点可以开始
            下一层的遍历.(重复上述过程,将哨兵节点记录下下层第一个节点,然后遍历该层,并把下面一层串起来)
        时间复杂度:O(n),每个节点均需处理一次
        空间复杂度:O(1),没有占用额外空间
        :param root: 原二叉树
        :return: 填充next指针后的二叉树
        """
        # curr初始化为根节点
        curr = root

        # 当前curr为下一层第一个节点,代表将遍历下一层.
        while curr:
            # 实例化哨兵节点
            dummy = Node()
            # tail初始化为哨兵节点(尾插法)
            tail = dummy

            # 遍历当前层的节点,并借助tail逐步后移串联起下一层
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                # 当前层下一个节点,通过next指针获取(实际当前层遍历等价于链表遍历)
                curr = curr.next
            # 哨兵节点持有的next即为下一层第一个节点
            curr = dummy.next

        return root
