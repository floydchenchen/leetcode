# 113. Path Sum II

# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
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
#  /  \    / \
# 7    2  5   1
# Return:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 这种find all的问题，用DFS最好
    # recursive DFS, backtrack
    def pathSum(self, root, sum):
        def dfs(root, sum, path, result):
            path.append(root.val)
            if not root.left and not root.right and sum == root.val:
                result.append(list(path))
            if root.left:
                dfs(root.left, sum - root.val, path, result)
            if root.right:
                dfs(root.right, sum - root.val, path, result)
            path.pop()

        result = []
        if not root:
            return result
        dfs(root, sum, [], result)
        return result

    # iterative DFS, stack
    def pathSum1(self, root, sum):
        result = []
        if not root:
            return result
        stack = [(root, sum - root.val, [root.val])]
        while stack:
            cur, val, path = stack.pop()
            if not cur.left and not cur.right and val == 0:
                result.append(path)
            if cur.left:
                stack.append((cur.left, val - cur.left.val, path + [cur.left.val]))
            if cur.right:
                stack.append((cur.right, val - cur.right.val, path + [cur.right.val]))
        return result

    # iterative BFS, queue
    def pathSum2(self, root, sum):
        result = []
        if not root:
            return result
        q = [(root, root.val, [root.val])]
        while q:
            cur, val, path = q.pop(0)
            if not cur.left and not cur.right and val == sum:
                result.append(path)
            if cur.left:
                q.append((cur.left, val + cur.left.val, path + [cur.left.val]))
            if cur.right:
                q.append((cur.right, val + cur.right.val, path + [cur.right.val]))
        return result
