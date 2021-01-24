# -*- coding: utf-8 -*-
"""
二叉树:根据前序和后续遍历构造二叉树
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        """
        思路: 递归方式进行.
        前序序列:(根节点,左子树前序序列,右子树前序序列)
        后序序列:(左子树后序序列,右子树后序序列,根节点)
        可根据左子树节点数相同进行子树的处理.设左子树长度为L,且左子树前序序列首元素与左子树后序序列尾元素一致.则可计算得到左子树节点数L
        L = post.index(pre[1]) + 1
        然后可根据L得出左子树的前序序列和后序序列,进行递归计算即可
        左子树:pre[1:L+1], post[0:L]
        右子树:pre[L+1:], post[L:len(post)-1]
        时间复杂度: O(n**2),每次递归均为获取长度l长度进行遍历
        空间复杂度: O(n**2),每次递归都借助了左右子树的前序/后序副本,导致空间复杂度较高
        :param pre: 前序遍历序列
        :param post: 后序遍历序列
        :return: 二叉树
        """
        # 前序序列为空,则直接返回None
        if not pre:
            return None

        # 使用前序序列首元素构造节点--即根节点
        node = TreeNode(pre[0])

        # 如果前序序列仅一个节点,则直接返回此节点
        if len(pre) == 1:
            return node

        # 计算左子树长度,用于后续递归切分子树前序/后序序列
        l = post.index(pre[1]) + 1

        # 对左子树进行递归计算,使用左子树前序序列和左子树后序序列
        node.left = self.constructFromPrePost(pre[1: l+1], post[0: l])
        # 对右子树进行递归计算,使用右子树前序序列和右子树后序序列
        node.right = self.constructFromPrePost(pre[l+1:], post[l:len(post) - 1])

        # 递归结束后返回结点即代表构建完成的二叉树
        return node


if __name__ == '__main__':
    pre = [1, 2, 4, 5, 3, 6, 7]
    post = [4, 5, 2, 6, 7, 3, 1]
    root = Solution().constructFromPrePost(pre, post)
    print(root)
