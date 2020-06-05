# 643. Maximum Average Subarray I

# Given an array consisting of n integers, find the contiguous subarray of
# given length k that has the maximum average value. And you need to output the maximum average value.
#
# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

from math import inf


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]

        # pre-sum list
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        nums = [0] + nums

        result = -inf
        # fixed length sliding window
        for j in range(k, len(nums)):
            result = max(result, (nums[j] - nums[j - k]) / k)
        return result
