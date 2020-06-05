# 329. Longest Increasing Path in a Matrix

# Given an integer matrix, find the length of the longest increasing path.
#
# From each cell, you can either move to four directions: left, right, up or down.
# You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
#
# Example 1:
#
# Input: nums =
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:
#
# Input: nums =
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

# 思路：dfs with memoization
class Solution:
    def longestIncreasingPath(self, matrix):
        def dfs(i, j, matrix, m, n, memo):
            if not memo[i][j]:
                val = matrix[i][j]
                memo[i][j] = 1 + max(
                    dfs(i + 1, j, matrix, m, n, memo) if i + 1 < m and val < matrix[i + 1][j] else 0,
                    dfs(i - 1, j, matrix, m, n, memo) if i and val < matrix[i - 1][j] else 0,
                    dfs(i, j + 1, matrix, m, n, memo) if j + 1 < n and val < matrix[i][j + 1] else 0,
                    dfs(i, j - 1, matrix, m, n, memo) if j and val < matrix[i][j - 1] else 0)
            return memo[i][j]

        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        return max(dfs(i, j, matrix, m, n, memo) for i in range(m) for j in range(n))
