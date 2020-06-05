# 152. Maximum Product Subarray
# Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
# which has the largest product.
#
# Example 1:
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

import math
class Solution:
   
    def maxProduct1(self, nums):
        _max = big = small = nums[0]
        for num in nums[1:]:
            # multiply by a negative number makes the small number bigger, big number smaller
            if num < 0:
                big, small = small, big
            big = max(num, num * big)
            small = min(num, num * small)
            _max = max(_max, big)
        return _max
