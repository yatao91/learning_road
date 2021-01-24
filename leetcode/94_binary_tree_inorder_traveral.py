# -*- coding: utf-8 -*-
"""二叉树中序遍历"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def recursionTraversal(self, root: TreeNode, res: List[int]):
        if root.left:
            self.recursionTraversal(root.left, res)
        res.append(root.val)
        if root.right:
            self.recursionTraversal(root.right, res)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        递归中序遍历,先进行左子树递归,当左子树不存在,则将当前结点值放入结果集;并判断右子树是否存在,存在则递归进行
        时间复杂度:O(n),对树的所有结点进行递归
        空间复杂度:最坏情况为O(n),平均情况为O(lgn)
        :param root:
        :return:
        """
        if not root:
            return []
        res = []
        self.recursionTraversal(root, res)

        return res

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        借助栈迭代遍历
        时间复杂度:O(n)
        空间复杂度:O(n)
        """
        # 结果容器
        res = []
        # 栈
        stack = []
        # 当前结点
        cur = root

        # 当前结点非空或栈非空
        while cur is not None or stack:
            # 当前结点非空则将当前结点入栈并指向左子结点
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            # 弹出当前栈顶部结点
            cur = stack.pop()
            # 添加到结果集
            res.append(cur.val)
            # 指向右子结点
            cur = cur.right

        return res

    def inorderTraversal3(self, root: TreeNode) -> List[int]:
        """
        莫里斯遍历--线索二叉树
        时间复杂度:O(n)
        空间复杂度:O(n),使用了长度为n的数组返回结果
        """
        cur = root
        res = []

        while cur is not None:

            if cur.left is None:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right is not None:
                    pre = pre.right

                temp = cur
                pre.right = cur
                cur = cur.left
                temp.left = None

        return res

    def inorderTraversal4(self, root: TreeNode) -> List[int]:
        """
        颜色标记法
        1.使用颜色标记节点的状态,新节点为白色,已访问的结点为灰色
        2.如果遇到的节点为白色,则将其标记为灰色,然后将其右子节点/自身/左子节点依次入栈
        3.如果遇到的节点为灰色,则将节点的值输出
        时间复杂度:O(n)
        空间复杂度:O(n),最坏情况下整棵树会压入栈中
        """
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

    def inorderTraversal5(self, root: TreeNode) -> List[int]:
        """
        pythonic颜色标记法改进版,使用类型判定进行
        中序遍历入栈顺序:右->节点->左, 出栈顺序:左->节点->右
        :param root:
        :return:
        """
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if isinstance(node, TreeNode):
                stack.extend([node.right, node.val, node.left])
            elif isinstance(node, int):
                res.append(node)
        return res


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3

    print(Solution().inorderTraversal5(root=node1))
