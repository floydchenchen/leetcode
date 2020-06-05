# 55. Jump Game

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# Example 1:
#
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.


# 每个element的值是这里能往前跳几格，看是否能到大于等于最后一格的地方


class Solution:
    # 方法1：从后往前搜，看是否能到达0
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= last:
                last = i
        return last == 0

    # 方法2：维护一个max_pos pointer，看max_pos是否能到达扫过的每一个点
    def canJump1(self, nums):
        max_pos = 0
        for i in range(len(nums)):
            if i > max_pos:
                return False
            max_pos = max(max_pos, nums[i] + i)
        return True