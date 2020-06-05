# 39. Combination Sum

# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(temp_list, result, candidates, remain, start):
            if remain < 0:
                return
            elif remain == 0:
                result.append(list(temp_list))
            else:
                for i in range(start, len(candidates)):
                    temp_list.append(candidates[i])
                    backtrack(temp_list, result, candidates, remain - candidates[i], i) # start with i, because we can re-use
                    temp_list.pop()
        result = []
        backtrack([], result, candidates, target, 0)
        return result