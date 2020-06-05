# 15. 3Sum

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution:
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		result = []
		# edge case
		if not nums or len(nums) < 3:
			return result

		# 3. 一定要先排序
		nums.sort()
		for i in range(0, len(nums) - 2):
			low, high, sum = i + 1, len(nums) - 1, -nums[i]
			# 1. skip duplicate nums[i]
			if i != 0 and nums[i - 1] == nums[i]:
				continue
			# 4. two-pointer 夹逼
			while low < high:
				# 5. 分大了、小了、刚好三种情况讨论
				# 小了
				if nums[low] + nums[high] < sum:
					low += 1
				# 大了
				elif nums[low] + nums[high] > sum:
					high -= 1
				# 刚好
				else:
					# add current combination to result list
					result.append([nums[i], nums[low], nums[high]])
					# 2. skip duplicates nums[low] and nums[high]
					while low < high and nums[low] == nums[low + 1]:
						low += 1
					while low < high and nums[high] == nums[high - 1]:
						high -= 1
					low += 1
					high -= 1
		return result

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))