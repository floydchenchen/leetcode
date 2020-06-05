# 81. Search in Rotated Sorted Array II

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
#
# You are given a target value to search. If found in the array return true, otherwise return false.
#
# Example 1:
#
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:
#
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false

# Follow up:
#
# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?

class Solution:
    def search(self, nums, target):
        if not nums:
            return False
        l, r = 0, len(nums) - 1
        while l <= r:
            # 跳过duplicate
            while l < r and nums[l] == nums[r]:  # 这样的目的是为了能准确判断mid位置，所以算法的最坏时间复杂度为O(n)
                l += 1
            mid = (l + r) // 2
            if target == nums[mid]:
                return True
            elif nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:  # 高区
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:  # 低区
                    l = mid + 1
                else:
                    r = mid - 1
        return False
