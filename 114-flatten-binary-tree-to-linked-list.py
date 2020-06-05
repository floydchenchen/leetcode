# 114. Flatten Binary Tree to Linked List

# Given a binary tree, flatten it to a linked list in-place.
#
# For example, given the following tree:
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6


# 思路：reverse-preorder traversal，因为原来的题要把所有的

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# -----------
# pre = 5
# cur = 4
#
#     1
#    /
#   2
#  / \
# 3   4
#      \
#       5
#        \
#         6
# -----------
# pre = 4
# cur = 3
#
#     1
#    /
#   2
#  /
# 3
#  \
#   4
#    \
#     5
#      \
#       6
# -----------
# cur = 2
# pre = 3
#
#     1
#    /
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
# -----------
# cur = 1
# pre = 2
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.prev = None

    # right -> left -> root reversed preorder去构建flattened tree
    def flatten_reverse_preorder(self, root):
        if not root:
            return None
        self.flatten_reverse_preorder(root.right)
        self.flatten_reverse_preorder(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root

    # left -> root -> right去构建
    def flatten_inorder(self, root):
        if not root:
            return
        self.prev = root
        self.flatten_inorder(root.left)

        temp = root.right
        root.right, root.left = root.left, None
        self.prev.right = temp

        self.flatten_inorder(temp)
