# 250. Count Univalue Subtrees

# Given a binary tree, count the number of uni-value subtrees.
#
# A Uni-value subtree means all nodes of the subtree have the same value.
#
# Example :
#
# Input:  root = [5,1,5,5,5,null,5]
#
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
#
# Output: 4

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0

        def is_uni(node):
            if not node:
                return True
            left, right = is_uni(node.left), is_uni(node.right)
            if left and right:
                if node.left and node.val != node.left.val:
                    return False
                if node.right and node.val != node.right.val:
                    return False
                self.count += 1
                return True
            return False

        is_uni(root)
        return self.count
