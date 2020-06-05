# 62. Unique Paths

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?

# Note: m and n will be at most 100.
#
# Example 1:
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# Example 2:
#
# Input: m = 7, n = 3
# Output: 28

# 思路：
# dp[i][j]：到grid[i][j]最多有几种走法
# 走到一个点只能从左边或者上面走过来，所以：dp[i][j] = dp[i-1][j] + dp[j-1][i]
class Solution:
    # O(n^2) space
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[-1][-1]

    # O(n) space
    # 空间优化思路：只有往下走和往右走，只用记录每一个row即可
    def uniquePaths1(self, m, n):
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]
        return dp[-1]