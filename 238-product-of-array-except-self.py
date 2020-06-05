# 238. Product of Array Except Self

# Given an array nums of n integers where n > 1,  return an array output such that output[i]
# is equal to the product of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]

# Could you solve it with constant space complexity?
# (The output array does not count as extra space for the purpose of space complexity analysis.)

class Solution:
    # two-pass, 左扫一遍，右扫一遍，核心是避开自己
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [None] * n
        result[0] = 1
        # product of all left elements except self
        for i in range(1, n):
            result[i] = nums[i-1] * result[i-1]
        right_temp = 1
        # product of all right elements except self
        for i in range(n-1, -1, -1):
            result[i] *= right_temp
            right_temp *= nums[i]
        return result




