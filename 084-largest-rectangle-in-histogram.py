# 84. Largest Rectangle in Histogram
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.

# Example:
#
# Input: [2,1,5,6,2,3]
# Output: 10

class Solution:
	def largestRectangleArea(self, heights):
		heights.append(0)
		# 维持一个单调递增栈
		stack, max_area = [-1], 0
		for i, h in enumerate(heights):
			while heights[stack[-1]] > h:
				max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
			stack.append(i)
		return max_area

print(Solution().largestRectangleArea([2,1,5,6,2,3]))