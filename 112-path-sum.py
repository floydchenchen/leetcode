# 112. Path Sum

# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values
# along the path equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # recursive solution, DFS
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right and sum - root.val == 0:
            return True
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    # iterative DFS, stack
    def hasPathSum1(self, root, sum):
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            cur, val = stack.pop()
            if not cur.left and not cur.right and val == sum:
                return True
            if cur.left:
                stack.append((cur.left, val + cur.left.val))
            if cur.right:
                stack.append((cur.right, val + cur.right.val))
        return False

    # iterative BFS, queue
    def hasPathSum2(self, root, sum):
        if not root:
            return False
        q = [(root, sum - root.val)]
        while q:
            cur, val = q.pop(0)
            if not cur.left and not cur.right and val == 0:
                return True
            if cur.left:
                q.append((cur.left, val - cur.left.val))
            if cur.right:
                q.append((cur.right, val - cur.right.val))
        return False
