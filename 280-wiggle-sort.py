# 280. Wiggle Sort

# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
#
# Example:
#
# Input: nums = [3,5,2,1,6,4]
# Output: One possible answer is [3,5,1,6,2,4]

# 思路：保证偶数位 => 奇数位 increase; 奇数位 => 偶数位 decrease，否则swap
#
class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            # 奇数位 XOR increase，注意这里的括号是必须的
            if (i % 2) ^ (nums[i] > nums[i-1]):
            # if (i % 2 == 0) != nums[i] > nums[i - 1]:
                # swap
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
