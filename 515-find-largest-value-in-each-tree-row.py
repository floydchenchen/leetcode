# 515. Find Largest Value in Each Tree Row

# You need to find the largest value in each row of a binary tree.

# Example:
# Input: 

#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 

# Output: [1, 3, 9]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import math
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        
        # level order traversal
        q = [root]
        while q:
            level_len = len(q)
            level_max = -math.inf
            for _ in range(level_len):
                node = q.pop(0)
                level_max = max(level_max, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level_max)
        return result