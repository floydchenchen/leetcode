# 45. Jump Game II

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
#
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Note:
#
# You can assume that you can always reach the last index.

class Solution:
    # greedy solution
    # 在每次的cur_end之内，找到这一跳的最远点cur_farthest，在到达i = cur_end时，更新下一个cur_end为cur_farthest，同时jums += 1
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = cur_end = cur_farthest = 0
        for i in range(len(nums) - 1):
            cur_farthest = max(cur_farthest, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = cur_farthest
        return jumps
