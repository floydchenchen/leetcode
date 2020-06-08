# 268. Missing Number
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1:
#
# Input: [3,0,1]
# Output: 2
# Example 2:
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

# Your algorithm should run in linear runtime complexity.
# Could you implement it using only constant extra space complexity?

class Solution:
	# 思路：x ^ x = 0，所以扫一遍，让result ^ 所有的i与nums[i]，这样找出missing number
	def missingNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		# 注意先把result设置成len(nums)，因为for-loop的i会错过len(nums)
		result = len(nums)
		for i in range(len(nums)):
			result ^= i
			result ^= nums[i]
		return result

sol = Solution()
print(sol.missingNumber([3,0,1]))

