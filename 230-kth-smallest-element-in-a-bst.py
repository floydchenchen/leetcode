# 230. Kth Smallest Element in a BST

# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Example 1:
#
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Example 2:
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
# How would you optimize the kthSmallest routine?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # count nodes number of left child, and then binary search
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def count_node(node):
            if not node:
                return 0
            return 1+ count_node(node.left) + count_node(node.right)

        left_count = count_node(root.left)
        if k <= left_count:
            return self.kthSmallest(root.left, k)
        elif k > left_count + 1:
            return self.kthSmallest(root.right, k - left_count - 1)
        else:
            return root.val
