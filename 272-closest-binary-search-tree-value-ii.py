# 272. Closest Binary Search Tree Value II

# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
# Example:
#
# Input: root = [4,2,5,1,3], target = 3.714286, and k = 2
#
#     4
#    / \
#   2   5
#  / \
# 1   3
#
# Output: [4,3]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # time O(n) solution
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        self.l = []
        self.helper(self.l, root, target, k)
        return self.l

    # return True if result is already found.
    def helper(self, l, node, target, k):
        """
        :type node: TreeNode
        :type target: float
        :type k: int
        :type l: list
        :rtype: bool
        """
        if not node:
            return False
        if self.helper(l, node.left, target, k):
            return True
        if len(l) == k:
            if abs(l[0] - target) < abs(node.val - target):
                return True
            else:
                l.pop(0)
        l.append(node.val)
        print(l)
        return self.helper(l, node.right, target, k)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(Solution().closestKValues(root, 3.7, 2))