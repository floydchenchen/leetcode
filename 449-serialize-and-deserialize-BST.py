# 449. Serialize and Deserialize BST

# Serialization is the process of converting a data structure or object into a sequence of bits so that
# it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed
# later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary search tree.
# There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that
# a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.
#
# The encoded string should be as compact as possible.
#
# Note: Do not use class member/global/static variables to store states.
# Your serialize and deserialize algorithms should be stateless.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
import math
class Codec:

    def serialize(self, root):
        vals = []

        def preOrder(node):
            if node:
                vals.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)

        return ' '.join(map(str, vals))

    # O(N) since each val run build once, preorder build
    def deserialize(self, data):
        vals = deque([int(val) for val in data.split()])

        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(minVal, val)
                node.right = build(val, maxVal)
                return node

        return build(-math.inf, math.inf)