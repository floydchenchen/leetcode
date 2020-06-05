# 209. Minimum Size Subarray Sum

# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of
# which the sum ≥ s. If there isn't one, return 0 instead.
#
# Example:
#
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

# two pointer，i pointer控制左边界，j pointer控制右边界
import math
class Solution:
    # two pointer O(n) solution
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i, j, _sum, min_len = 0, 0, 0, math.inf

        while j < len(nums):
            _sum += nums[j]
            j += 1
            while _sum >= s:
                min_len = min(min_len, j - i)
                _sum -= nums[i]
                i += 1

        return 0 if min_len == math.inf else min_len

    # presum list and binary search solution O(nlgn)
    def minSubArrayLen1(self, s, nums):
        def binary_search(l, r, key, nums):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= key:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        # presum list
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        min_len = math.inf
        for i in range(len(nums)):
            # 注意处理找不到的情况
            end = binary_search(i+1, len(nums) - 1, nums[i] + s, nums)
            if end == len(nums):
                break
            min_len = min(min_len, end - i)
        return 0 if min_len == math.inf else min_len

