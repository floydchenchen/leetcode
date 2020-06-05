# 11. Container With Most Water
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
# which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.

# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
class Solution:
	# two pointer, sliding window, 夹逼
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		l, r = 0, len(height) - 1
		max_area = 0

		while l < r:
			max_area = max(max_area, min(height[l], height[r]) * (r - l))
			# 哪边height小，更新哪边
			# 03-29-2020，因为如果更新height大那边，并没有机会让maxArea变大，因为maxArea受较矮的一边限制
			if height[l] < height[r]:
				l += 1
			else:
				r -= 1
		return max_area