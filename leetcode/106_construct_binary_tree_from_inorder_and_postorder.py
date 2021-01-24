# -*- coding: utf-8 -*-
"""
构造二叉树:从中序和后序遍历序列构造二叉树
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        思路:递归构造二叉树.
        时间复杂度:O(n)
        空间复杂度:O(n),存储整棵树
        """
        def helper(in_left, in_right):
            if in_left > in_right:
                return None

            val = postorder.pop()
            root = TreeNode(val)

            index = idx_map[val]

            # 先处理右子树,再处理左子树.后续遍历:[left,right,root],逆序构造二叉树:[root,right,left]
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)

            return root

        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)

    def buildTree2(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def recursionBuildTree(post_left: int, post_right: int, in_left: int, in_right: int):
            """
            递归构造子树
            :param post_left: 子树后序序列左边界
            :param post_right: 子树后序序列右边界
            :param in_left: 子树中序序列左边界
            :param in_right: 子树中序序列右边界
            :return:
            """
            # 树左边界大于右边界,表示树为空,返回None
            if in_left > in_right or post_left > post_right:
                return None

            # 后续遍历根节点索引即后续序列右边界
            post_root_index = post_right

            # 从中序遍历hashmap中获取中序遍历根节点索引
            inorder_root_index = idx_map[postorder[post_root_index]]

            # 构造根节点
            root = TreeNode(postorder[post_root_index])

            # 计算左子树节点个数:中序序列根节点位置 - 中序遍历左边界
            size_left_sub = inorder_root_index - in_left

            # 递归构造左子树,并连接到root左节点
            # 后序序列左右边界:[左边界,左边界+左子树结点数-1]
            # 中序序列左右边界:[左边界,根节点-1]
            root.left = recursionBuildTree(post_left=post_left,
                                           post_right=post_left + size_left_sub - 1,
                                           in_left=in_left,
                                           in_right=inorder_root_index - 1)
            # 递归构造右子树,并连接到root右节点
            # 后序序列左右边界:[左边界+左子树节点数,右边界-1]
            # 中序序列左右边界:[根节点+1,右边界]
            root.right = recursionBuildTree(post_left=post_left + size_left_sub,
                                            post_right=post_right - 1,
                                            in_left=inorder_root_index + 1,
                                            in_right=in_right)

            return root

        n = len(inorder)
        idx_map = {val: idx for idx, val in enumerate(inorder)}

        return recursionBuildTree(0, n - 1, 0, n - 1)


if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    print(Solution().buildTree2(inorder, postorder))
