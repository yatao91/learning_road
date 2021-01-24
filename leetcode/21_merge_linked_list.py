# -*- coding: UTF-8 -*-
"""
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        思路:采用递归形式进行,如果l1的首元素小于l2的首元素,则转化为l1的首元素与l1后续链表与l2链表的合并操作
        时间复杂度:O(m+n),m和n是两链表的长度,每次递归都会去掉两链表之一的头结点
        空间复杂度:O(m+n),递归调用消耗栈空间,栈空间大小取决于递归调用的深度.最多调用m+n次.
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoLists2(self, l1, l2):
        """
        思路:迭代比较.通过将结果移动到哨兵结点后方便后续返回合并后的链表.
        时间复杂度:O(m+n)
        空间复杂度:O(1)
        """
        prehead = ListNode(-1)
        prev = prehead
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 else l2
        return prehead.next
