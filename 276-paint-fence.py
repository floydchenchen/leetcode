# 276. Paint Fence

# There is a fence with n posts, each post can be painted with one of the k colors.
#
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
#
# Return the total number of ways you can paint the fence.
#
# Note:
# n and k are non-negative integers.
#
# Example:
#
# Input: n = 3, k = 2
# Output: 6
# Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:
#
#             post1  post2  post3
#  -----      -----  -----  -----
#    1         c1     c1     c2
#    2         c1     c2     c1
#    3         c1     c2     c2
#    4         c2     c1     c1
#    5         c2     c1     c2
#    6         c2     c2     c1


# Its easier to think in terms of state transition diagram. Every post i can end in diff state or same state.
# Think of the state transition between i-1 and i.
#
# If prev state was diff, then current state can end in diff or same.
# diff(i-1) -> diff(i)
# diff(i-1) -> same(i)
#
# If prev state was same then current state can only end in diff.
# same(i-1) -> diff(i)

class Solution:
	def numWays(self, n, k):
		if not n:
			return 0
		if n == 1:
			return k
		same, diff = k * 1, k * (k - 1)
		for i in range(3, n + 1):
			same, diff = diff, (diff + same) * (k - 1)
		return same + diff

