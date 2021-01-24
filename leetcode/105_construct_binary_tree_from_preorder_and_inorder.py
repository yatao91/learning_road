# -*- coding: utf-8 -*-
"""
二叉树:从前序和中序遍历序列构造二叉树
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        思路:递归求解.
        时间复杂度:O(n)
        空间复杂度:O(n)
        """
        def helper(in_left, in_right):
            if in_left > in_right:
                return None

            val = preorder.pop(0)
            index = idx_map[val]

            root = TreeNode(val)
            root.left = helper(in_left, index - 1)
            root.right = helper(index + 1, in_right)

            return root

        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        思路:
        1.前序遍历结果为:[根节点,[左子树前序遍历结果],[右子树前序遍历结果]]
        2.中序遍历结果为:[[左子树中序遍历结果],根节点,[右子树中序遍历结果]]
        3.同一棵树的前序遍历结果和中序遍历结果长度相同(节点数一样,肯定相同啊),可以据此进行定位
        由前序遍历可得根节点root,然后通过根节点root在中序遍历序列中进行定位.然后就可以知道左子树的前序遍历和中序遍历结果,右子树的前序遍历和中序遍历
        结果.此时,就可以采用递归的形式,递归的构造出左子树和右子树,再将两棵子树接到根节点的左右位置.

        时间复杂度:O(n)
        空间复杂度:O(n),除去返回答案需要的O(n)空间之外,还需要O(n)空间存储哈希映射,以及O(h)(h是树的高度)的空间表示递归时栈空间.h<n,所以为O(n)
        """
        def recursionBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            """
            递归构建树函数
            :param preorder_left: 树的前序遍历结果左边界
            :param preorder_right: 树的前序遍历结果右边界
            :param inorder_left: 树的中序遍历结果左边界
            :param inorder_right: 树的中序遍历结果右边界
            :return: 树的根节点
            """
            # 左边界大于右边界时,即子树为空,返回None(前序序列或中序序列均可作为判断条件来作为递归终止条件)
            if preorder_left > preorder_right:
                return None

            # 前序遍历根节点位置即前序遍历左边界
            preorder_root = preorder_left
            # 使用根节点值从前序序列构造的hashmap中获取根节点位置
            inorder_root = idx_map[preorder[preorder_root]]
            # 构造根节点
            root = TreeNode(preorder[preorder_root])
            # 计算中序遍历左子树节点个数:[中序遍历根节点位置 - 中序遍历左边界位置] 同一棵树每种遍历方式节点数均一致
            size_left_subtree = inorder_root - inorder_left

            # 递归构造左子树,并连接到root左节点
            # 前序序列左右边界:[左边界+1,左边界+左子树元素个数]
            # 中序序列左右边界:[左边界,根节点-1]
            root.left = recursionBuildTree(preorder_left + 1,
                                           preorder_left + size_left_subtree,
                                           inorder_left,
                                           inorder_root - 1)
            # 递归构造右子树,并连接到root右节点
            # 前序序列左右边界:[左边界+左子树元素个数+1,右边界]
            # 中序序列左右边界:[根节点+1,右边界]
            root.right = recursionBuildTree(preorder_left + size_left_subtree + 1,
                                            preorder_right,
                                            inorder_root + 1,
                                            inorder_right)

            return root

        n = len(preorder)
        idx_map = {val: idx for idx, val in enumerate(inorder)}

        return recursionBuildTree(0, n - 1, 0, n - 1)


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(Solution().buildTree2(preorder, inorder))
