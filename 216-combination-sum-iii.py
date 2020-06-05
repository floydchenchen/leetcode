# 216. Combination Sum III

# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Note:
#
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Example 2:
#
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]

class Solution:
    # DFS, backtracking method
    def combinationSum3(self, k, n):
        def backtrack(temp_list, result, start, remain, k):
            if remain < 0:
                return
            elif remain == 0 and len(temp_list) == k:
                result.append(list(temp_list))
            else:
                for i in range(start, 9 + 1):
                    temp_list.append(i)
                    backtrack(temp_list, result, i + 1, remain - i, k)
                    temp_list.pop()
        result = []
        backtrack([], result, 1, n, k)
        return result
