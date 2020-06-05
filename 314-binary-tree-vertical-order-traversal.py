# 314. Binary Tree Vertical Order Traversal

# Given a binary tree, return the vertical order traversal of its nodes' values.
# (ie, from top to bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from left to right.
#
# Examples 1:
#
# Input: [3,9,20,null,null,15,7]
#
#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7
#
# Output:
#
# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]
# Examples 2:
#
# Input: [3,9,8,4,0,1,7]
#
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#
# Output:
#
# [
#   [4],
#   [9],
#   [3,0,1],
#   [8],
#   [7]
# ]
# Examples 3:
#
# Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)
#
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#     /\
#    /  \
#    5   2
#
# Output:
#
# [
#   [4],
#   [9,5],
#   [3,0,1],
#   [8,2],
#   [7]
# ]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict
class Solution:
    # BFS, level order traversal with dictionary to store node values at each columns
    def verticalOrder(self, root):
        cols = defaultdict(list)
        q = [(root, 0)]
        while q:
            node, i = q.pop(0)
            if node:
                cols[i].append(node.val)
                if node.left:
                    q.append((node.left, i - 1))
                if node.right:
                    q.append((node.right, i + 1))
        return [cols[i] for i in sorted(cols)]
