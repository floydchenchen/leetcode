# 377. Combination Sum IV

# Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
#
# Example:
#
# nums = [1, 2, 3]
# target = 4
#
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
#
# Note that different sequences are counted as different combinations.
#
# Therefore the output is 7.
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?

# 思路：
# dp[i]: sum为i时，最多有几个组合
# 对nums中的每一个num，如果 num <= i，那么dp[i] += dp[i - num]
class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [1] + [0] * target
        for i in range(1, len(dp)):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        return dp[-1]

