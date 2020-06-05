# 46. Permutations

# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution:
	# DFS, backtracking method
	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""

		def backtrack(nums, temp_list, result):
			# base / exit
			if len(temp_list) == len(nums):
				# 一定不能直接append tem_list，因为这里的temp_list是by reference，一定要新建一个list
				result.append(list(temp_list))
			else:
				for num in nums:
					if num not in temp_list:
						temp_list.append(num)
						backtrack(nums, temp_list, result)
						temp_list.pop()

		result = []
		if not nums:
			return result

		backtrack(nums, [], result)
		return result


	def permute_2(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""

		def backtrack(nums, temp_list, result):
			# base / exit
			if len(temp_list) == len(nums):
				# 一定不能直接append tem_list，因为这里的temp_list是by reference，一定要新建一个list
				result.append(list(temp_list))
			else:
				for num in nums:
					if not (num in temp_list):
						temp_list.append(num)
						backtrack(nums, temp_list, result)
						temp_list.pop()

		result = []
		if len(nums) == 0 or not nums:
			return result

		backtrack(nums, [], result)
		return result