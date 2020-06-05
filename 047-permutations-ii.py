# 47. Permutations II

# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example:
#
# Input: [1,2,1]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

class Solution:
	def permuteUnique(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		def backtrack(nums, temp_list, result, used):
			# base / exit
			if len(temp_list) == len(nums):
				# 一定不能直接append tem_list，因为这里的temp_list是by reference，一定要新建一个list
				result.append(list(temp_list))
			else:
				for i in range(len(nums)):
					# 如果当前值在backtrack中被用过，或者当前值和上第一个值相同（同时上一个值没用过）来避免重复
					# 例如此时result中已经有[1,1,2] (used: [1,0,0]), 这时候我们用第二个1的时候，（used[0]已经重新变成了0）,
					# 此时再加起来就会重复
					print(nums)
					if used[i] or i > 0 and nums[i] == nums[i-1] and not used[i-1]:
						continue
					else:
						used[i] = 1
						temp_list.append(nums[i])
						backtrack(nums, temp_list, result, used)
						used[i] = 0
						temp_list.pop()

		result = []
		if not nums:
			return result
		nums.sort()
		backtrack(nums, [], result, [0] * len(nums))
		return result

sol = Solution()
print(sol.permuteUnique([1,1,2]))