# -*- coding: utf-8 -*-
"""
二叉树的最近公共祖先
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        思路:
        1.使用哈希表存储每个节点及其父节点.(递归DFS)
        2.针对节点p,根据哈希表获取对应的父节点信息并不断的往上跳,使用集合存储途径的父节点
        3.针对节点q,同样根据哈希表获取对应的父节点信息不断往上跳,如果访问的祖先已经存在p节点访问过的,即为p和q节点的最近公共祖先节点.即LCA节点
        时间复杂度:O(n)
        空间复杂度:O(n),最坏情况下当树为链式时,递归调用栈最深为n.
        :param root: 二叉树
        :param p: 节点p
        :param q: 节点q
        :return: 节点p和节点q最近公共祖先节点
        """
        parent = {}
        visited = set()

        def dfs(node: 'TreeNode'):
            if not node:
                return
            if node.left:
                parent[node.left.val] = node
                dfs(node.left)
            if node.right:
                parent[node.right.val] = node
                dfs(node.right)

        dfs(root)

        while p:
            visited.add(p)
            p = parent.get(p.val)

        while q:
            if q in visited:
                return q
            q = parent.get(q.val)


    ans = None

    def dfs(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool:
        # 节点为空,则直接返回False
        if not root:
            return False
        # 调用递归函数,对左子树进行递归处理
        lson = self.dfs(root.left, p, q)
        # 调用递归函数,对右子树进行递归处理
        rson = self.dfs(root.right, p, q)
        # 当p与q存在于某结点的左子树和右子树中,或当前节点为p节点或q节点,且当前节点的左子树或右子树有一个包含了另一个节点的情况,即为LCA节点
        if (lson and rson) or ((root.val == p.val or root.val == q.val) and (lson or rson)):
            self.ans = root

        # 上一层递归返回结果:节点左孩子或右孩子中含有p节点或q节点,或节点为p节点或q节点
        return (lson or rson) or (root.val == p.val or root.val == q.val)

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        思路:递归遍历二叉树.
        最近公共祖先节点x满足以下性质:
        1.节点x的左子树和右子树均包含p节点或q节点
        2.或者:节点x恰好是p节点或q节点,且左子树或右子树有一个包含了另一个节点的情况
        公共祖先深度是否最大?
        是最大的.因为递归是自底向上从叶子节点开始更新的,所有满足条件的公共祖先一定是深度最大的祖先最先被访问到.
        时间复杂度:O(n),二叉树每一个节点只会被访问一次.
        空间复杂度:O(n),递归调用的栈空间取决于二叉树的高度,二叉树最坏情况下为一条链,此时高度与节点数相同.因此最坏空间复杂度为O(n)
        :param root: 二叉树
        :param p: 二叉树节点p
        :param q: 二叉树节点q
        :return: 最近公共祖先节点
        """
        # 1.递归遍历二叉树
        self.dfs(root, p, q)

        # 2.返回最近公共祖先节点
        return self.ans

    def lowestCommonAncestor3(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        思路:采用递归遍历.遍历左右子树,并判定是否为p节点或q节点.
        1.p节点在节点x的左子树,q节点在节点x的右子树,则节点x为最近公共祖先节点(自底向上)
        时间复杂度:O(n),访问每个节点
        空间复杂度:O(n),递归调用栈空间在树为链式结构时,递归调用栈空间最大,最坏空间复杂度为O(n)
        :param root: 二叉树
        :param p: 二叉树p节点
        :param q: 二叉树q节点
        :return: 最近公共祖先节点
        """
        if root == p or root == q:
            return root

        if root:
            lNode = self.lowestCommonAncestor3(root.left, p, q)
            rNode = self.lowestCommonAncestor3(root.right, p, q)
            if lNode and rNode:  # p,q节点分别在左右子树中,父节点即为最近公共祖先节点
                return root
            elif lNode is None:  # 两节点都在右子树
                return rNode
            else:  # 两节点都在左子树
                return lNode

        return None
