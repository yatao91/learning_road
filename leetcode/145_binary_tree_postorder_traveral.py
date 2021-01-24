# -*- coding: utf-8 -*-
"""二叉树-后序遍历"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def recursionTraversal(self, node: TreeNode, res: List[int]):
        if node.left:
            self.recursionTraversal(node.left, res)
        if node.right:
            self.recursionTraversal(node.right, res)
        res.append(node.val)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        思路:递归遍历,左子结点存在则进入左子树递归;右子结点存在则进入右子树递归;均不存在,则加入结果集中
        时间复杂度:O(n),会递归每一个节点
        空间复杂度:O(n),递归调用栈为O(n),因对每一个节点递归
        """
        res = []
        if root is None:
            return []
        self.recursionTraversal(root, res)
        return res

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        思路:借助辅助栈迭代遍历形式,基于BFS宽度优先搜索,逐层入栈并出栈加入到结果集中,考虑到逆序,则输出结果集的逆序
        时间复杂度:O(n),因要对每一个节点进行遍历
        空间复杂度:O(n),最坏空间复杂度为O(n),当树某种结构时比如完全二叉树,则栈中最大元素数量为O(n/2)即为O(n).
        """
        if root is None:
            return []

        stack, res = [root, ], []

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res[::-1]


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3
    print(Solution().postorderTraversal2(root=node1))
