# 73. Set Matrix Zeroes

# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
#
# Example 1:
#
# Input:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# Example 2:
#
# Input:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# Follow up:
#
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

# 思路： store states of each row in the first of that row,
# and store states of each column in the first of that column.
# 对于row0和col0共用同一个cell，新建一个col0即可


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col0, rows, cols = 1, len(matrix), len(matrix[0])

        # 将每个row和col的信息储存到col和row的第0个
        for i in range(rows):
            if not matrix[i][0]:
                col0 = 0
            for j in range(1, cols):
                if not matrix[i][j]:
                    matrix[i][0] = matrix[0][j] = 0

        # top-down update，这样不影响col和row的第0个
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, 0, -1):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
            if not col0:
                matrix[i][0] = 0

Solution().setZeroes([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
])

# Solution().setZeroes([
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ])