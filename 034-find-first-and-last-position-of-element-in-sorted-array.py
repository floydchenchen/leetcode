# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in ascending order, find the starting and ending position of a
# given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

class Solution:
    def searchRange(self, nums, target):
        # 第二类： 找到第一个不小于目标值的数，可变形为查找最后一个小于目标值的数
        def binarySearchLeft(nums, x):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        # 找到最后一个不大于目标值的数
        def binarySearchRight(nums, x):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= x:
                    l = mid + 1
                else:
                    r = mid - 1
            return r

        l, r = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (l, r) if l <= r else [-1, -1]