# 33. Search in Rotated Sorted Array
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# binary search，target可能所处的三个位置需要r = i - 1：
# 注意小于与小于等于的区别（nums[i] 这里一定是 < nums[0]，因为这个是pivot的定义）
# nums[0] <= target <= nums[i]                       ==> sorted order
#            target <= nums[i] < nums[0]
#                      nums[i] < nums[0] <= target

# 跟普通的第一类binary search比较像，但是需要注意的是搜索的时候array是经过翻转过的
# 因为是第一类binary search，所以和nums[mid]作比较时，一定不能包含等号，另外两个比较时无所谓
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= target < nums[mid] or target < nums[mid] < nums[0] or nums[mid] < nums[0] <= target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
