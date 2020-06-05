# 85. Maximal Rectangle

# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
# Example:
#
# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6


# 思路：对每一排进行maximal rectangle in histogram的查找
class Solution:
    # dp solution
    def maximalRectangle(self, matrix):
        max_area = 0
        if not matrix or not matrix[0]:
            return max_area

        n = len(matrix[0])
        # 对每一排进行maximal rectangle in histogram的查找
        heights = [0] * (n + 1)
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == "1" else 0
            stack = [-1]
            for i, h in enumerate(heights):
                while heights[stack[-1]] > h:
                    max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
                stack.append(i)
        return max_area

