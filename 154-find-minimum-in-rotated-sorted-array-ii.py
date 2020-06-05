# 154. Find Minimum in Rotated Sorted Array II

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# The array may contain duplicates.
#
# Example 1:
#
# Input: [1,3,5]
# Output: 1
# Example 2:
#
# Input: [2,2,2,0,1]
# Output: 0
# Note:
#
# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?

class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            # move the right pointer if nums[m] == nums[r]
            else:
                r = r - 1
        return nums[l]
