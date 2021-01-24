# -*- coding: utf-8 -*-
"""
对称二叉树
https://leetcode-cn.com/problems/symmetric-tree/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def check(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and self.check(p.left, q.right) and self.check(p.right, q.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        """
        思路:使用递归形式解此题.
        如果判断一个树为镜像对称的
        1.两个根结点具有相同的值
        2.每个树的右子树均与另一个树的左子树镜像对称
        时间复杂度:O(n)
        空间复杂度:O(n)
        """
        if root is None:
            return True
        return self.check(root.left, root.right)

    def check2(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [p, q]
        while stack:
            p = stack.pop()
            q = stack.pop()
            if p is None and q is None:
                continue
            if (p is None or q is None) or p.val != q.val:
                return False
            stack.extend([p.left, q.right])
            stack.extend([p.right, q.left])
        return True

    def isSymmetric2(self, root: TreeNode) -> bool:
        """
        思路:使用辅助栈进行迭代二叉树,代替递归形式.引入队列首先将根结点放入两次,然后队列非空时,则从队列中拿取两个元素比较是否镜像对称.然后将各结点
        的左右子结点按相反的顺序放入队列,进行循环.当判断非镜像对称树时,直接退出循环并返回
        时间复杂度:O(n)
        空间复杂度:需要一个队列来维护结点,每个结点最多进队一次,出队一次,队列中最多不会超过n个点.渐进空间复杂度为O(n)
        """
        return self.check2(root, root)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    node6 = TreeNode(4)
    node7 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    print(Solution().isSymmetric2(root=node1))
