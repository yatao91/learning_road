# -*- coding: utf-8 -*-
"""二叉树-层序遍历"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        思路:双队列模式
        时间复杂度:
        空间复杂度:
        """
        if not root:
            return []
        stack, res = [root, ], []

        while stack:
            temp_res = []
            temp_stack = []

            for node in stack:
                temp_res.append(node.val)
                if node.left:
                    temp_stack.append(node.left)
                if node.right:
                    temp_stack.append(node.right)

            res.append(temp_res)
            stack = temp_stack

        return res

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        """
        思路:采用BFS(宽度优先搜索),逐层遍历二叉树.并借助队列的形式存放树节点,每层开始放入前,根据队列长度一次遍历完放入结果集及补充下一层节点
        时间复杂度:O(n),每个节点都会入一次栈
        空间复杂度:O(n),队列中的节点说不会超过n个.
        """
        if not root:
            return []
        stack, res = [root, ], []
        while stack:
            level = []
            length = len(stack)
            for i in range(length):
                node = stack.pop(0)
                level.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(level)

        return res


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.right = node5
    print(Solution().levelOrder2(node1))
