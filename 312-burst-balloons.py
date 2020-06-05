# 312. Burst Balloons

# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
# You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
# Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# Input: [3,1,5,8]
# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

# ideas: 1. nums[out_of_range] = 1
# let the last balloon to burst to be nums[i],  for the last we have nums[-1]*nums[i]*nums[n]
# We can see that the balloons is again separated into 2 sections.
# But this time since the balloon i is the last balloon of all to burst,
# the left and right section now has well defined boundary and do not affect each other!
# Therefore we can do either recursive method with memoization or dp.


class Solution:
    # dp solution, O(n^3) time, O(n^2) space
    def maxCoins(self, iNums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + [i for i in iNums if i > 0] + [1]
        n = len(nums)
        # dp[i][j] is the max point in range nums[i:j+1]
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        return dp[0][-1]




