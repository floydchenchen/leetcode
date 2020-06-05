# 53. Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


# idea: We want to find a sequence of days over which the net change from the first day to the last is maximum
import math
class Solution:
    # greedy solution / simplified dp solution
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sum = 0
        max_sum = -math.inf
        for i in range(len(nums)):
            if sum < 0:
                sum = nums[i]
            else:
                sum += nums[i]

            max_sum = max(max_sum, sum)

        return max_sum

    # divide and conquer solution
    # Divide-and-conquer suggests that we divide the subarray into two subarrays of as equal size as possible.
    # use a mid point, then maxSubarray exists in one of nums[start:mid], nums[mid:end] or nums[start:end]
    # https://raw.githubusercontent.com/floydchenchen/pictures/master/Screen%20Shot%202018-07-15%20at%2011.12.17%20AM.png
    def maxSubArray_v2(self, nums):
        return self.max_subarray_divide_and_conquer(nums, 0, len(nums) - 1)

    def max_subarray_divide_and_conquer(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = left + (right - left) // 2
        left_sum = self.max_subarray_divide_and_conquer(nums, left, mid)
        right_sum = self.max_subarray_divide_and_conquer(nums, mid + 1, right)
        cross_sum = self.find_max_crossing_subarray(nums, left, right)
        return max(left_sum, right_sum, cross_sum)

    def find_max_crossing_subarray(self, nums, left, right):
        left_sum, right_sum, temp_sum = -math.inf, -math.inf, 0
        mid = left + (right - left) // 2

        for i in range(mid, left - 1, -1):
            temp_sum += nums[i]
            left_sum = temp_sum if temp_sum > left_sum else left_sum

        temp_sum = 0
        for i in range(mid + 1, right + 1):
            temp_sum += nums[i]
            right_sum = temp_sum if temp_sum > right_sum else right_sum

        return left_sum + right_sum

sol = Solution()
new_list = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray_v2(new_list))
