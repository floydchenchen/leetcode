# 145. Binary Tree Postorder Traversal

# Given a binary tree, return the postorder traversal of its nodes' values.
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
# Output: [3,2,1]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # iterative stack solution: the opposite of preorder
    # left -> right -> root
    def postorderTraversal(self, root):
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            node = stack.pop()
            # 先左再右
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            result = [node.val] + result
        return result

    def postorderTraversal1(self, root):
        def postorder_recursive(root, result):
            if not root:
                return
            postorder_recursive(root.left, result)
            postorder_recursive(root.right, result)
            result.append(root.val)
            
        result = []
        postorder_recursive(root, result)
        return result