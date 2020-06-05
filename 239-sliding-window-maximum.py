# 239. Sliding Window Maximum
# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the
# very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
#
# Example:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# 过程
# i = 0 => window: [0:0] q: [{0: 1}], result = []
# i = 1 => window: [0:1] q: [{1: 3}], result = []
# i = 2 => window: [0:2] q: [{1: 3}, {2: -1}], result = [3]
# i = 3 => window: [1:3] q: [{1: 3}, {2: -1}, {3: -3}], result = [3, 3]
# i = 4 => window: [2:4] q: [{4: 5}], result = [3, 3, 5]
# i = 5 => window: [3:5] q: [{4: 5}, {5: 3}], result = [3, 3, 5, 5]
# i = 6 => window: [4:6] q: [{6: 6}], result = [3, 3, 5, 5, 6]
# i = 7 => window: [5:7] q: [{7: 7}], result = [3, 3, 5, 5, 6, 7]

# 思路：用单调递减的deque来保存这个window，注意deque中存的是元素的index而不是元素的值
from collections import deque
class Solution:
	def maxSlidingWindow(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		result = [0] * (len(nums) - k + 1)
		if k < 1 or k > len(nums):
			return []
		index = 0
		# 单调递减的deque来记录元素的index
		q = deque()
		# i相当于window的右边界，i+1-k相当于window的左边界
		for i in range(len(nums)):
			# 如果queue中第一个值出了window左边界，remove之
			while q and q[0] < i+1-k:
				q.popleft()
			# 如果新的值大于queue尾部的一些值，remove掉这些尾部的值，因为它们不可能成为max
			while q and nums[i] > nums[q[-1]]:
				q.pop()
			q.append(i)
			# 如果左边界>=0，说明是时候把window的max放进result了
			if i+1-k >= 0:
				result[index] = nums[q[0]]
				index += 1
		return result

sol = Solution()
print(sol.maxSlidingWindow([7,2,4],2))