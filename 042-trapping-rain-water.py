# 42. Trapping Rain Water

class Solution:
	def trap(self, height):
		"""
        :type height: List[int]
        :rtype: int
        """
		stack, area, temp_area, i = [], 0, 0, 0
		while i < len(height):
			# 如果高度持续下降，那么要继续往stack上加，直到找到底部
			if not stack or height[i] <= height[stack[-1]]:
				stack.append(i)
				i += 1
			# 如果高度有上升，那么我们形成了一个sink，开始计算面积，其中底部是stack[-1]
			else:
				bot = stack.pop()
				temp_area = 0 if not stack else (i - stack[-1] - 1) * (min(height[stack[-1]], height[i]) - height[bot])
				area += temp_area
		return area

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))