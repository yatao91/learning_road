# -*- coding: utf-8 -*-
"""
LeetCode104.二叉树的最大深度
https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    ans = 0

    def recursionDepth(self, node: TreeNode, depth: int):
        if not node.left and not node.right:
            self.ans = max(self.ans, depth)
        if node.left:
            self.recursionDepth(node.left, depth + 1)
        if node.right:
            self.recursionDepth(node.right, depth + 1)

    def maxDepth(self, root: TreeNode) -> int:
        """
        思路:采用"自顶向下"递归处理,根节点深度为1,其下一层节点深度加一,当节点为叶子节点时,使用depth深度更新结果值ans(注意需定义为类变量或全局变量)
        时间复杂度:O(n),因需遍历到每一个节点,所以时间复杂度为O(n)
        空间复杂度:O(n),当树结构特殊时,比如最左树/最右树,递归调用函数栈将于节点数一致,则递归调用栈为n,空间复杂度为O(n)
        """
        if not root:
            return self.ans
        self.recursionDepth(root, 1)
        return self.ans

    def maxDepth2(self, root: TreeNode) -> int:
        """
        思路:采用"自底向上"递归处理,如果想知道根节点树深度,那么知道了根节点左右子树的深度然后用最大值加一即可.所以可递归处理到最底部,然后依次往上进行
        时间复杂度:O(n),因需对树所有节点递归进行调用
        空间复杂度:O(height),递归函数需要栈空间,而栈空间取决于递归的深度,因此空间复杂度等于二叉树的高度.
        """
        if not root:
            return 0
        left_depth = self.maxDepth2(root.left)
        right_depth = self.maxDepth2(root.right)

        return max(left_depth, right_depth) + 1

    def maxDepth3(self, root: TreeNode) -> int:
        """
        思路:采用BFS"广度优先搜索",因要求取树的深度,不再是进行层次数据的返回.可维护一个深度计数值,将每层入栈的元素清理完毕后深度计数加一进行下一层元素出栈
        时间复杂度:O(n),因遍历的为二叉树的所有节点,所以时间复杂度为O(n)
        空间复杂度:O(n),空间消耗取决于栈空间的消耗,最坏情况下会达到O(n).比如完全二叉树,一次入栈两个,出栈一个,最多是有n/2个节点在栈中
        """
        ans = 0
        if not root:
            return ans

        stack = [root, ]
        while stack:
            size = len(stack)
            for i in range(size):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            ans += 1

        return ans


if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    print(Solution().maxDepth3(node1))
