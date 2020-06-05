# 41. First Missing Positive

# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
# Input: [1,2,0]
# Output: 3
# Example 2:
#
# Input: [3,4,-1,1]
# Output: 2
# Example 3:
#
# Input: [7,8,9,11,12]
# Output: 1

# Your algorithm should run in O(n) time and uses constant extra space.

class Solution:
    # two pass solution
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Pass 1, move every value to the position of its value (in-place in nums)
        # 类似于bucket sort
        n = len(nums)
        for i in range(n):
            target = nums[i]
            while 1 <= target <= n and target != nums[target - 1]:
                # 注意这样写不对！，我估计因为给list赋值涉及到pointer，和给variable赋值不同
                # 这样写的话，target会改变，导致nums[target - 1]得到错误的值
                # target, nums[target - 1] = nums[target - 1], target
                nums[target - 1], target = target, nums[target - 1]

        # Pass 2, find first location where the index doesn't match the value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

sol = Solution()
print(sol.firstMissingPositive([3,4,-1,1]))


