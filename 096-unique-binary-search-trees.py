# 96. Unique Binary Search Trees

# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
#
# Example:
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# 思路：DP
# dp[i]: the maximum number of BST trees built from 1 ... i
# transition: 对从1到i的每一个数j，如果拿j当root，那么left child的最多组合为dp[j-1]，right child的最多组合为dp[i-j]，
# 所以此时dp[i] += dp[j - 1] * dp[i - j]

# The essential process is: to build a tree, we need to pick a root node,
# then we need to know how many possible left sub trees and right sub trees can be held under that node,
# finally multiply them.
class Solution:
    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        #
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
