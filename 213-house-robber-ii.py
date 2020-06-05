# 213. House Robber II

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of
# money stashed. All houses at this place are arranged in a circle. That means the first house is the
# neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will
# automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
#
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
#              because they are adjacent houses.
# Example 2:
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

# https://leetcode.com/problems/house-robber/discuss/186274/state-machine-dp-solution-with-image-and-explanation
# 思路：
# if there are 0, 1, 2, ..., n-1, n houses, robbers either rob the first house or do not rob the first house:
#
# If robbers rob the first house, we rob from 0, 1, 2, ..., n-1 houses.
# If robbers do not rob the first house, we rob from 1, 2, ..., n-1, n houses.
class Solution:
	# state machine dp solution
	def rob(self, nums):
		def rob_in_line(nums):
			s0 = s1 = 0
			for num in nums:
				s0, s1 = max(s0, s1), s0 + num
			return max(s0, s1)
		if len(nums) == 1:
			return nums[0]
		return max(rob_in_line(nums[:-1]), rob_in_line(nums[1:]))
