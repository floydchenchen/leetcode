# 18. 4Sum

# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
# such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution:
	# 用类似DFS的方法，一层一层的reduce n 的数量
	def nSum(self, nums, target, n, current_list, result):
		# edge case
		if n < 2 or len(nums) < n:
			return

		# 2sum，注意像普通3sum，需要考虑duplicate
		if n == 2:
			start, end = 0, len(nums) - 1
			while start < end:
				if nums[start] + nums[end] == target:
					# 注意这里不要忘了current_list
					result.append(current_list + [nums[start], nums[end]])
					start += 1
					end -= 1

					# avoid duplicates（连续的相同元素）
					while start < end and nums[start] == nums[start - 1]:
						start += 1
					while start < end and nums[end] == nums[end + 1]:
						end -= 1
				elif nums[start] + nums[end] < target:
					start += 1
				else:
					end -= 1

		# n-sum (n > 2)
		else:
			# 注意range的范围
			for i in range(0, len(nums) - n + 1):
				# 优化：看是否能直接略过
				if target > nums[-1] * n or target < nums[i] * n:
					break
				# avoid duplicate
				if i == 0 or i > 0 and nums[i-1] != nums[i]:
					self.nSum(nums[i+1:], target - nums[i], n - 1, current_list + [nums[i]], result)

	def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		nums.sort()
		result = []
		self.nSum(nums, target, 4, [], result)
		return result