# -*- coding: utf-8 -*-
"""二叉树前序遍历"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        采用迭代方式,使用一个栈数据结构存放遍历到的结点,每次从栈出弹出一个放入结果集中.需要注意的是入栈顺序应该是右孩子先入栈,左孩子再入栈,
        以保证结点输出顺序符合前序遍历顺序
        时间复杂度:O(n),n为树结点数量.每个结点都将遍历一次
        空间复杂度:O(n),n为树结点数量.最坏空间复杂度即遍历完整棵树存储整棵树,取决于树的结构.TODO 没有理解最坏空间复杂度
        :param root:
        :return:
        """
        if root is None:
            return []

        stack, output = [root], []

        while stack:
            node = stack.pop()
            if node is not None:
                output.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        return output

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        莫里斯遍历 TODO 不懂
        时间复杂度: O(N)
        空间复杂度: O(1)
        :param root:
        :return:
        """
        # 1.初始化当前结点为根结点,数据结果为空列表
        node, output = root, []

        # 2.当node非None时while循环,否则返回数据结果
        while node:
            # 2.1.当前结点左子节点不存在,则将当前结点值添加到数据结果中,并向右移动
            if not node.left:
                output.append(node.val)
                node = node.right
            # 2.2.当前结点左子节点存在,则记录左子节点为当前结点的中序遍历前驱结点
            else:
                predecessor = node.left

                # 2.2.1.左子节点存在后,则沿右子节点一直向下访问,直到右子节点为空或右子节点与当前结点相同
                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right

                # 2.2.2.右子节点为空,则添加当前结点值到数据结果,并建立右子节点到当前结点的伪边并更新前驱结点为下一个点
                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node
                    node = node.left
                # 2.2.3.右子节点非空,则右子节点与当前结点相同,则拆除伪边并向右移动
                else:
                    predecessor.right = None
                    node = node.right
        return output

    def recursionTraveral(self, root: TreeNode, res: List[int]):
        res.append(root.val)
        if root.left:
            self.recursionTraveral(root.left, res)
        if root.right:
            self.recursionTraveral(root.right, res)

    def preorderTraversal3(self, root: TreeNode) -> List[int]:
        """
        递归进行二叉树前序遍历,每次保存结点值,并先对左子树进行递归,再对右子树进行递归
        时间复杂度:O(N),递归会递归每一个节点,二叉树节点数为n,所以时间复杂度为O(N)
        空间复杂度:O(N),最坏空间复杂度为O(N),比如全是左子树或全是右子树;如果为完全二叉树,则为O(lgN)
        :param root:
        :return:
        """
        if not root:
            return []
        res = []
        self.recursionTraveral(root, res)
        return res


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.left = node2
    node1.right = node5
    node2.left = node3
    node2.right = node4

    print(Solution().preorderTraversal3(root=node1))
