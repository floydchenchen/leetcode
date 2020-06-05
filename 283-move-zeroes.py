# 283. Move Zeroes

# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # i是最左边的0的pointer
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            print(nums)

sol = Solution()
print(sol.moveZeroes([0,1,0,3,12]))