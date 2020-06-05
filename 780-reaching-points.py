# 780. Reaching Points

# A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).
#
# Given a starting point (sx, sy) and a target point (tx, ty), return True if and only
# if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.
#
# Examples:
# Input: sx = 1, sy = 1, tx = 3, ty = 5
# Output: True
# Explanation:
# One series of moves that transforms the starting point to the target is:
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
#
# Input: sx = 1, sy = 1, tx = 2, ty = 2
# Output: False
#
# Input: sx = 1, sy = 1, tx = 1, ty = 1
# Output: True


# one reaching point.
# 机器人初始坐标（x1,y1）目标（x2,y2）。（x1,y1>1）。行动模式（x+y,y）或（x,y+x）。问是否能到达目标。
# 递归，若最终 x1 > x2 或 y1 > y2 则不可能到达。
#
# 思路：从(M, N) 出发，M 和 N 必定一大一小，否则不可能满足上述条件。所以两者中较大是 X + Y， 较小是 X 或 Y。
# 由此从右下往左上反推，每一步都只可能有一个路径，所以最终能到达(x1, y1)则为 True

class Solution:
	# 超时了
	def reachingPoints(self, x1, y1, x2, y2):
		# final step is (x, x+y) or (x+y, x)
		def reach_previous_pos(x, y):
			if x > y:  # (x+y, x)
				return x - y, y
			else:  # (x, x+y)
				return x, y - x

		if x2 == y2:
			return False
		while x2 >= x1 and y2 >= y1:
			x2, y2 = reach_previous_pos(x2, y2)
			if x1 == x2 and y1 == y2:
				return True
		return False

	# 改进一下，不用减法，用%
	# I cut down one by one at first and I got TLE. So I came up with remainder.
	# 评论：Impressive! It looks like a tree, if you know one node,
	# it's always easy to get the root because you have exact one way to get the parent node.
	def reachingPoints1(self, x1, y1, x2, y2):
		while x1 <= x2 and y1 <= y2:
			x2, y2 = x2 % y2, y2 % x2
		return x1 == x2 and (y2 - y1) % x1 == 0 or y1 == y2 and (x2 - x1) % y1 == 0

print(Solution().reachingPoints1(3,3,12,9))