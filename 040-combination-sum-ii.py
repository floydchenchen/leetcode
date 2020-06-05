# 40. Combination Sum II

# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def backtrack(candidates, temp_list, result, start, remain):
            if remain < 0:
                return
            elif remain == 0:
                result.append(list(temp_list))
            else:
                for i in range(start, len(candidates)):
                    # 跳过连续的重复元素
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    temp_list.append(candidates[i])
                    # 从i+1开始，因为不可以重复同一元素
                    backtrack(candidates, temp_list, result, i + 1, remain - candidates[i])
                    temp_list.pop()

        result = []
        # candidate是有重复一定要先sort
        backtrack(sorted(candidates), [], result, 0, target)
        return result