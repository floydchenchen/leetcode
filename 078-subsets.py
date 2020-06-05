# 78. Subsets

# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution:
	# DFS, backtracking method
	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		def backtrack(nums, temp_list, result, start):
			result.append(list(temp_list)) # append first to include "[]"
			for i in range(start, len(nums)):
				temp_list.append(nums[i])
				# 因为是set，为了避免重复，下一个start从i+1开始
				backtrack(nums, temp_list, result, i + 1)
				temp_list.pop()

		result = []
		if not nums:
			return result

		backtrack(nums, [], result, 0)
		return result

sol = Solution()
print(sol.subsets([1,2,3,]))