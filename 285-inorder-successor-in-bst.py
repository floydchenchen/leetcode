# 285. Inorder Successor in BST

# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
#
# Note: If the given node has no in-order successor in the tree, return null.
#
# Example 1:
#
# Input: root = [2,1,3], p = 1
#
#   2
#  / \
# 1   3
#
# Output: 2
# Example 2:
#
# Input: root = [5,3,6,2,4,null,null,1], p = 6
#
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1
#
# Output: null


class Solution:
    def inorderSuccessor(self, root, p):
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ