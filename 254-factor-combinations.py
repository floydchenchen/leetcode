# 254. Factor Combinations
# Numbers can be regarded as product of its factors. For example,
#
# 8 = 2 x 2 x 2;
#   = 2 x 4.
# Write a function that takes an integer n and return all possible combinations of its factors.
#
# Note:
#
# You may assume that n is always positive.
# Factors should be greater than 1 and less than n.
# Example 1:
#
# Input: 1
# Output: []
# Example 2:
#
# Input: 37
# Output:[]
# Example 3:
#
# Input: 12
# Output:
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]
# Example 4:
#
# Input: 32
# Output:
# [
#   [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]
# ]

class Solution:
    # 超时
    def getFactors(self, n):

        def backtrack(temp_list, result, start, remain):
            if remain <= 1:
                if len(temp_list) > 1:
                    result.append(list(temp_list))
            else:
                for i in range(start, remain + 1):
                    if remain % i == 0:
                        temp_list.append(i)
                        backtrack(temp_list, result, i, remain // i)
                        temp_list.pop()

        result = []
        backtrack([], result, 2, n)
        return result

    # iterative backtracking
    def getFactors1(self, n):
        ans, stack, x = [], [], 2
        while True:
            if x > n / x:
                if not stack:
                    return ans
                ans.append(stack + [n])
                x = stack.pop()
                n *= x
                x += 1
            elif n % x == 0:
                stack.append(x)
                n /= x
            else:
                x += 1