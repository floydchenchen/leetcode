# 64. Minimum Path Sum

# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

# dp[i][j]: grid[i][j]这个位置的最小path sum
# transition: dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
# 可以直接用grid来当dp table，注意考虑边界情况
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                # 考虑边界情况
                if not i and not j:
                    continue
                elif not i and j:
                    grid[i][j] += grid[i][j - 1]
                elif not j and i:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]
