# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not preorder:
            return None
        root = TreeNode(preorder.pop(0))
        inorder_index = inorder.index(root.val)
        root.left = self.buildTree(preorder, inorder[:inorder_index])
        root.right = self.buildTree(preorder, inorder[inorder_index + 1:])
        return root


sol = Solution()
print(sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))

