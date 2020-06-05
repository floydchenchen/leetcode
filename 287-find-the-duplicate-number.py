# 287. Find the Duplicate Number

# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
# prove that at least one duplicate number must exist. Assume that there is only one duplicate number,
# find the duplicate one.
#
# Example 1:
#
# Input: [1,3,4,2,2]
# Output: 2
# Example 2:
#
# Input: [3,1,3,4,2]
# Output: 3
# Note:
#
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.

# 思路：binary search，每次找到mid值，再扫一遍nums，找到 <= mid值的数的count，如果count <= mid，说明duplicate > mid，
# 继续从mid + 1开始找；反之亦然
class Solution:
    # binary search方法
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 1, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                l = mid + 1
            else:
                r = mid - 1
        return l