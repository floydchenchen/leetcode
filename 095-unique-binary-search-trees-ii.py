# 95. Unique Binary Search Trees II

# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
#
# Example:
#
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1, n + 1)

    def dfs(self, start, end):
        if start == end:
            return [None]
        result = []
        # for every node as root
        for i in range(start, end):
            left = self.dfs(start, i)
            print("left", left)
            right = self.dfs(i + 1, end)
            print("right", right)
            for l in left:
                for r in right:
                    node = TreeNode(i)
                    node.left, node.right = l, r
                    result.append(node)
        return result


sol = Solution()
print(sol.generateTrees(3))
