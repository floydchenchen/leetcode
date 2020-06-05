# 98. Validate Binary Search Tree

# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#
# Input:
#     2
#    / \
#   1   3
# Output: true
# Example 2:
#
#     5
#    / \
#   1   4
#      / \
#     3   6
# Output: false
# Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
#              is 5 but its right child's value is 4.


# 注意
#    10
#    / \
#   5  15
#      / \
#     6   20
# Output: false

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import math
class Solution:
    def isValidBST(self, root):

        # 正确做法：将left的最大值和right的最小值存起来，同root比较
        def isValidBSTHelper(root, l_max, r_min):
            if not root:
                return True
            if root.val >= r_min or root.val <= l_max:
                return False
            return isValidBSTHelper(root.left, l_max, root.val) and isValidBSTHelper(root.right, root.val, r_min)

        return isValidBSTHelper(root, -math.inf, math.inf)
