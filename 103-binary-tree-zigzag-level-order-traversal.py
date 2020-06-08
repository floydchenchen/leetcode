# 103. Binary Tree Zigzag Level Order Traversal

# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # BFS
    def zigzagLevelOrder(self, root):
        q = []
        result = []
        if not root:
            return result

        q.append(root)
        rev = False
        while q:
            level_list = []
            level_size = len(q)
            # 不能直接用 range(len(q))，因为len(q)会变！
            for _ in range(level_size):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if rev:
                    level_list = [node.val] + level_list 
                else:
                    level_list.append(node.val)
            result.append(level_list)
            rev = not rev

        return result