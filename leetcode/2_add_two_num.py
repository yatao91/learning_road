# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1.预先指针,用来相加完成后返回和链表头指针
        pre = ListNode(0)
        cur = pre
        # 2.进位变量
        carry = 0

        while l1 is not None or l2 is not None:
            # 1.获取l1结点和l2结点值,不存在则置为0
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # 2.与进位一起求和
            sum = x + y + carry

            # 3.计算新进位值,并将整除10的余数作为下一个结点的值
            carry = sum // 10
            sum = sum % 10
            cur.next = ListNode(sum)

            # 4.将当前结点置为下一结点
            cur = cur.next

            # 5.获取下一结点值
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        # 遍历完后,如果进位值为1,则补到链表之后
        if carry == 1:
            cur.next = ListNode(carry)

        # 返回头结点
        return pre.next
