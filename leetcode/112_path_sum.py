# -*- coding: utf-8 -*-
"""
二叉树:路径总和问题
https://leetcode-cn.com/problems/path-sum/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        思路:当考虑路径和的时候,可以从根结点开始,如果根结点不满足和,则考虑根结点后的树是否满足.所以采用递归模式进行.
        时间复杂度:O(n),n为树的节点数.对每个节点访问一次
        空间复杂度:O(H),H为树高.空间复杂度主要考虑递归时栈空间的开销.最坏情况下,树为链状,空间复杂度为O(n),平均情况下
                 树的高度与节点数的对数有关,空间复杂度为O(lgn).
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    def hasPathSum2(self, root: TreeNode, sum: int) ->bool:
        """
        思路:采用广度优先搜索(BFS),借助两个辅助队列进行比较
        时间复杂度:O(n),遍历树的所有节点
        空间复杂度:O(n),取决于队列空间开销,不会超过树的节点数.
        """
        if not root:
            return False
        node_queue = [root, ]
        val_queue = [root.val, ]

        while node_queue:
            node = node_queue.pop(0)
            val = val_queue.pop(0)
            if not node.left and not node.right:
                if val == sum:
                    return True
                continue
            if node.left:
                node_queue.append(node.left)
                val_queue.append(val + node.left.val)
            if node.right:
                node_queue.append(node.right)
                val_queue.append(val + node.right.val)

        return False


if __name__ == '__main__':
    node1 = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(8)
    node4 = TreeNode(11)
    node5 = TreeNode(13)
    node6 = TreeNode(4)
    node7 = TreeNode(7)
    node8 = TreeNode(2)
    node9 = TreeNode(1)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.left = node5
    node3.right = node6
    node4.left = node7
    node4.right = node8
    node6.right = node9

    print(Solution().hasPathSum2(node1, 22))
