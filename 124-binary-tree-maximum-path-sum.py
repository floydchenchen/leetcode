# 124. Binary Tree Maximum Path Sum

# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node
# in the tree along the parent-child connections. The path must contain at least one node and
# does not need to go through the root.
#
# Example 1:
#
# Input: [1,2,3]
#
#        1
#       / \
#      2   3
#
# Output: 6 (2-1-3)
# Example 2:
#
# Input: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: 42 (15-20-7)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import math


class Solution:
    # 将问题转化为：从某个node开始往下走，left path sum + right path sum + node.val
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # Helper updating a "global" maximum
        # 注意考虑负数！
        def helper(node):
            if not node:
                return 0
            left_path = max(0, helper(node.left))
            right_path = max(0, helper(node.right))
            self.max = max(self.max, left_path + node.val + right_path)
            # return的部分是为了求left_path和right_path用
            return max(left_path, right_path) + node.val

        self.max = -math.inf
        helper(root)
        return self.max
