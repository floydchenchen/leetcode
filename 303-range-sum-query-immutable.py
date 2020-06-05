# 303. Range Sum Query - Immutable

# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        # pre-sum array
        for i in range(1, len(nums)):
            self.nums[i] += self.nums[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.nums[j] - (self.nums[i - 1] if i > 0 else 0)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
