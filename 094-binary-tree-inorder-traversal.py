# 94. Binary Tree Inorder Traversal

# Given a binary tree, return the inorder traversal of its nodes' values.
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
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursive inorder traversal
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder_recursive(root, result):
            if not root:
                return
            inorder_recursive(root.left, result)
            result.append(root.val)
            inorder_recursive(root.right, result)

        result = []
        inorder_recursive(root, result)
        return result

    # iterative inorder traversal: stack
    def inorderTraversal1(self, root):
        result, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            result.append(node.val)
            root = node.right
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.right = TreeNode(6)

sol = Solution()
print(sol.inorderTraversal1(root))