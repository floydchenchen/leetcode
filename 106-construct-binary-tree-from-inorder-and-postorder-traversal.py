# 106. Construct Binary Tree from Inorder and Postorder Traversal

# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursive solution: postorder's last index is root, then find the inorder index according to root val
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())
        inorderIndex = inorder.index(root.val)
        # since postorder is left -> right -> root, we start from right
        # 这样每次pop postorder最后一个的时候，能保证是right subtree的root
        root.right = self.buildTree(inorder[inorderIndex + 1:], postorder)
        root.left = self.buildTree(inorder[:inorderIndex], postorder)
        return root
