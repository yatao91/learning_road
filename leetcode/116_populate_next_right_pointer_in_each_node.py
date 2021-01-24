# -*- coding: utf-8 -*-
"""
二叉树:填充每个节点的下一个右侧节点指针
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        思路:采用BFS广度优先搜索(层序遍历),逐层填充next指针.
        使用根节点初始化栈,然后计算每层节点数length,使用length做range遍历,针对遍历出的每个节点,进行指针填充.并将此节点的右子节点和左子节点
        添加到栈中.
        关键点: 避免下一层节点影响上一层节点的填充工作
            1.出栈从队首出
            2.入栈先入右子节点,然后入左子节点
        时间复杂度: O(n),遍历树的所有节点
        空间复杂度: O(n),完美二叉树,最后一个层级包含节点数为n/2个.广度优先遍历的空间复杂度取决于一个层级上的最大元素数量.丢弃常数,复杂度为O(n)
        :param root: 原二叉树
        :return: 填充后二叉树
        """
        # 二叉树为空,直接返回空
        if not root:
            return None

        # 使用根节点初始化迭代辅助栈
        stack = [root, ]

        # 栈非空时进行循环迭代
        while stack:
            # 计算栈大小,用于下面的迭代
            length = len(stack)
            # 后一节点引用,非空时用于前一节点的连接工作
            pre = None

            # 迭代栈
            for _ in range(length):
                # 每次迭代则将首元素拿出来(其实是后面的节点)
                node = stack.pop(0)
                # 后一节点存在,则加入到当前结点next指针后
                if pre:
                    node.next = pre
                # 将当前节点赋予pre
                pre = node
                # 先将右子节点入栈
                if node.right:
                    stack.append(node.right)
                # 再将左子节点入栈
                if node.left:
                    stack.append(node.left)

        return root

    def connect2(self, root: 'Node') -> 'Node':
        """
        思路: 使用已建立的next指针,对树的下层节点进行next连接.
        时间复杂度:O(n),每个节点只访问一次
        空间复杂度:O(1),不涉及到辅助栈的使用
        :param root: 原二叉树
        :return: 填充next指针后的二叉树
        """
        # 根节点为空,则直接返回None
        if not root:
            return root

        # 初始最左节点为根节点
        leftmost = root

        # 最左节点无左孩子时即代表已填充完整棵树(完美二叉树)
        while leftmost.left:

            # 针对树的每层处理相当于遍历链表,每层链表头部指向当前最左节点
            head = leftmost

            # 遍历当前层链表
            while head:

                # 同一父节点下的两个子节点直接进行next连接
                head.left.next = head.right

                # 获取当前节点next节点,针对不同父节点,则左侧父节点右孩子与右侧父节点左孩子进行next连接
                if head.next:
                    head.right.next = head.next.left

                # 移动head头到下一节点(next指针)
                head = head.next

            # 移动最左节点到下一层
            leftmost = leftmost.left

        # 遍历完成后返回根节点
        return root

    def connect3(self, root: 'Node') -> 'Node':
        """
        思路:采用递归解法(DFS).
        从根节点开始,左右节点不断向下深入,left节点不断往右走,right节点不断往左走,当两个节点走到底后
        整个纵深即完成串联.
        终止条件:当前节点为空
        函数内:以当前节点为起始,完成从上往下的纵深串联,再递归的对当前节点的left和right进行调用
        时间复杂度: O(n),访问了二叉树的每一个节点
        空间复杂度: O(h),h为二叉树高度
        :param root: 二叉树
        :return: 完成连接的二叉树
        """
        def dfs(root):
            if not root:
                return
            left = root.left
            right = root.right

            while left:
                left.next = right
                left = left.right
                right = right.left
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return root

    def connect4(self, root: 'Node') -> 'Node':
        def dfs(node: 'Node'):
            if not node or not node.left:
                return
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return root
