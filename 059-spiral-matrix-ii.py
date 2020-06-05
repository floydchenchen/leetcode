# 59. Spiral Matrix II

# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

# 思路:
#     ||  =>  |9|  =>  |8|      |6 7|      |4 5|      |1 2 3|
#                      |9|  =>  |9 8|  =>  |9 6|  =>  |8 9 4|
#                                          |8 7|      |7 6 5|
class Solution:
    def generateMatrix(self, n):
        A, lo = [], n * n + 1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [range(lo, hi)] + zip(*A[::-1])
        return A

