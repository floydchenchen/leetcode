# 429. N-ary Tree Level Order Traversal

# Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example, given a 3-ary tree:
#
#
#
#
#
#
#
# We should return its level order traversal:
#
# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


# iterative BFS solution
class Solution:
    def levelOrder(self, root):
        q = []
        result = []
        if not root:
            return result
        q.append(root)

        while q:
            level_list = []
            level_size = len(q)
            for _ in range(level_size):
                node = q.pop(0)
                for child in node.children:
                    q.append(child)
                level_list.append(node.val)
            result.append(level_list)
        return result
