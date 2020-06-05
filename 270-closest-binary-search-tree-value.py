# 270. Closest Binary Search Tree Value

# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.
# Example:
#
# Input: root = [4,2,5,1,3], target = 3.714286
#
#     4
#    / \
#   2   5
#  / \
# 1   3
#
# Output: 4

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # iterative binary search method
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        result = root.val
        while root:
            if abs(root.val - target) < abs(result - target):
                result = root.val
            root = root.left if target < root.val else root.right
        return result

    # recursive
    def closestValue1(self, root, target):
        self.result = root.val
        def closest(node, target):
            if not node:
                return self.result
            if abs(node.val - target) < abs(self.result - target):
                self.result = node.val
            if target < node.val:
                closest(node.left, target)
            else:
                closest(node.right, target)

        closest(root, target)
        return self.result

