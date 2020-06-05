# 628. Maximum Product of Three Numbers

# Given an integer array, find three numbers whose product is maximum and output the maximum product.
#
# Example 1:
# Input: [1,2,3]
# Output: 6
# Example 2:
# Input: [1,2,3,4]
# Output: 24

# 思路：找到最大的3个和最小的2个（因为有可能有负数）
import math
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2 = max3 = -math.inf
        min1 = min2 = math.inf

        for num in nums:
            # max
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num

            # min
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
        return max(max1 * max2 * max3, max1 * min1 * min2)


