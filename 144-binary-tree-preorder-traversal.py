# 144. Binary Tree Preorder Traversal

# Given a binary tree, return the preorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursive
    # root -> left -> right
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        result.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return result

    # iterative stack
    # 为什么要用stack，并且将先append node.right，这样先pop node.left，实现preorder
    def preorderTraversal1(self, root):
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
