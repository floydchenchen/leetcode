# 54. Spiral Matrix

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# 1. extract the first row
# 2. rotate the remaining matrix counter-clockwise

#     |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
#     |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
#     |7 8 9|      |4 7|

#     |1 2 3|      |6 9|      |8 7|      |4|      |5|

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # one-line solution
        # return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

        if not matrix:
            return []

        temp_matrix = []
        for j in range(len(matrix[0]) - 1, -1, -1):
            temp_row = []
            for i in range(1, len(matrix), 1):
                temp_row.append(matrix[i][j])
            temp_matrix.append(temp_row)
            print(temp_matrix)

        return matrix[0] + self.spiralOrder(temp_matrix)

sol = Solution()
print(sol.spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]))