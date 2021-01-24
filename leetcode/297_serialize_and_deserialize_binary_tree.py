# -*- coding: utf-8 -*-
"""
二叉树的序列化和反序列化
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def preorder_serialize(self, root, tree_str):
        if not root:
            tree_str += "None,"
        else:
            tree_str += str(root.val) + ","
            tree_str = self.preorder_serialize(root.left, tree_str)
            tree_str = self.preorder_serialize(root.right, tree_str)
        return tree_str

    def serialize(self, root):
        tree_str = self.preorder_serialize(root, "")
        return tree_str

    def deserialize(self, data):
        pass



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
