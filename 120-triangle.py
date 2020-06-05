# 120. Triangle

# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers
# on the row below.
#
# For example, given the following triangle
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space,
# where n is the total number of rows in the triangle.

# dp[i][j]是从下往上到这个位置的最小的path sum，可以利用triangle将空间优化为O(1)
# transition: dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i, -1, -1):
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]