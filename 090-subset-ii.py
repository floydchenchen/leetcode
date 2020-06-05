# 90. Subsets II

# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(nums, temp_list, result, start):
            result.append(list(temp_list))
            for i in range(start, len(nums)):
                # 避免重复：略过连续的相同元素
                if i > start and nums[i] == nums[i-1]:
                    continue
                temp_list.append(nums[i])
                backtrack(nums, temp_list, result, i + 1)
                temp_list.pop()

        result = []
        if not nums:
            return result

        # nums.sort()
        backtrack(sorted(nums), [], result, 0)
        return result
