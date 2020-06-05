# 16. 3Sum Closest

# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest
# to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
# Example:
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
	def threeSumClosest(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		# edge case
		if not nums or len(nums) < 3:
			return 0

		result = nums[0] + nums[1] + nums[2]
		# 1. sort
		nums.sort()
		for i in range(len(nums) - 2):
			# 3. two-pointer 夹逼
			low, high = i + 1, len(nums) - 1
			while low < high:
				sum = nums[i] + nums[low] + nums[high]
				if sum > target:
					high -= 1
				else:
					low += 1
				# 2. 每次while-loop最后，根据与target的距离，更新result即可
				result = sum if abs(sum - target) < abs(result - target) else result
		return result
