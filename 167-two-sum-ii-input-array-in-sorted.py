# 167. Two Sum II - Input array is sorted

class Solution:
	# two pointer method, 类似于3sum的方法
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		# edge case
		if not nums or len(nums) < 2:
			return None
		# two-pointer夹逼
		low, high = 0, len(nums) - 1
		while low < high:
			s = nums[low] + nums[high]
			if s == target:
				return [low + 1, high + 1]
			elif s > target:
				high -= 1
			else:
				low += 1