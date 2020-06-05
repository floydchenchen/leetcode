# 226. Invert Binary Tree

# Invert a binary tree.
#
# Example:
#
# Input:
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursive, divide and conquer
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        # divide and conquer
        # 这里一定要写成1行，不然需要temp去存root.right的值（因为它会改变）
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    # BFS, level order traversal
    def invertTree1(self, root):
        if not root:
            return root

        q = [root]
        while q:
            node = q.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root

    # iterative DFS, stack
    def invertTree2(self, root):
        if not root:
            return root

        stack = [root]

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
