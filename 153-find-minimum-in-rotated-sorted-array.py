# 153. Find Minimum in Rotated Sorted Array

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Example 1:
#
# Input: [3,4,5,1,2]
# Output: 1
#
#
# Example 2:
#
# Input: [4,5,6,7,0,1,2]
# Output: 0

# 这个题不能用 while l <= r，因为我们要找到是一个min值
class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            # 因为是rotated，所以这样最小值在m的右边
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
