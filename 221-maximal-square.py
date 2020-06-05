# 221. Maximal Square

# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
# Example:
#
# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4

# 思路：
# dp[i][j]: 以matrix[i][j]为右下角的点最大能够组成多大的square
# dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
# 也就是说如果matrix[i][j]是"1"的话，那么需要满足左、上、左上三个点全部都是square，才能增加一个新的square
#
# above  above-left  left
#
#  1111     1111
#  1111     1111     1111
#  1111     1111     1111
#  1111     1111     1111
#     *         *    1111*

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_len = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                # 注意边界
                if matrix[i][j] and i and j:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1
                max_len = max(max_len, matrix[i][j])
        return max_len * max_len


