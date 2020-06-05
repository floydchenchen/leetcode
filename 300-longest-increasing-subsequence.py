# 300. Longest Increasing Subsequence

# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Example:
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

class Solution:
    # dp[i] stores the smallest tail of all increasing subsequences with length (i+1).
    # For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:
    #
    # len = 1   :      [4], [5], [6], [3]   => dp[0] = 3
    # len = 2   :      [4, 5], [5, 6]       => dp[1] = 5
    # len = 3   :      [4, 5, 6]            => dp[2] = 6

    # binary search and dp solution
    def lengthOfLIS(self, nums):
        dp = [0] * len(nums)
        size = 0
        for num in nums:
            l, r = 0, size - 1
            # binary search
            while l <= r:
                m = (l + r) // 2
                if dp[m] < num:
                    l = m + 1
                else:
                    r = m - 1
            # num的插入位置
            dp[l] = num
            size = max(l + 1, size)
            print(dp)
        return size


sol = Solution()
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
