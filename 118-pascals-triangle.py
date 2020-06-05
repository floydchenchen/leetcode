# 118. Pascal's Triangle

# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
# 解法：
#   0 1      0 1 1     0 1 2 1
# + 1 0    + 1 1 0   + 1 2 1 0
# ------   -------     -------
#   1 1      1 2 1     1 3 3 1

class Solution:
    def generate(self, numRows):
        if not numRows:
            return []
        result = [[1]]
        for i in range(1, numRows):
            # 给每一层的list左右加0.再相加
            result += [list(map(lambda x, y: x + y, result[-1] + [0], [0] + result[-1]))]
            print(result)
        return result
print(Solution().generate(5))