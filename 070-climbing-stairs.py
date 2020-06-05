# 70. Climbing Stairs

# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# 思路：
# dp[i]: 到第i阶有最多有几种跳法
# dp[i] = dp[i-1] + dp[i-2]
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # for n >= 2, reduce dp space to O(1)
        # f(n) = f(n-1) + f(n-2)
        dp = [1, 1]
        for _ in range(n):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]

        return dp[0]
