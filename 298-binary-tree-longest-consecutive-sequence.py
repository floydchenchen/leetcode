# 298. Binary Tree Longest Consecutive Sequence

# Given a binary tree, find the length of the longest consecutive sequence path.
#
# The path refers to any sequence of nodes from some starting node to any node in the tree along the
# parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).
#
# Example 1:
#
# Input:
#
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
#
# Output: 3
#
# Explanation: Longest consecutive sequence path is 3-4-5, so resulturn 3.
# Example 2:
#
# Input:
#
#    2
#     \
#      3
#     /
#    2
#   /
#  1
#
# Output: 2
#
# Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so resulturn 2.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import math
class Solution:
    # preorder iterative stack DFS
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        result = 0
        stack = [(root, 1)]
        while stack:
            node, count = stack.pop()
            if node.left:
                stack.append((node.left, count + 1 if node.left.val == node.val + 1 else 1))
            if node.right:
                stack.append((node.right, count + 1 if node.right.val == node.val + 1 else 1))
            result = max(result, count)

        return result

    # preorder recursive DFS
    def longestConsecutive1(self, root):

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            max_left = 1 + left if root.left and root.left.val - root.val == 1 else 1
            max_right = 1 + right if root.right and root.right.val - root.val == 1 else 1
            self.result = max(self.result, max(max_left, max_right))
            return max(max_left, max_right)

        if not root:
            return 0
        self.result = -math.inf
        dfs(root)
        return self.result

