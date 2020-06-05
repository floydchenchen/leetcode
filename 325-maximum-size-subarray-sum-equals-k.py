# 325. Maximum Size Subarray Sum Equals k

# Given an array nums and a target value k, find the maximum length of a subarray that sums to k.
# If there isn't one, return 0 instead.
#
# Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.
#
# Example 1:
#
# Input: nums = [1, -1, 5, -2, 3], k = 3
# Output: 4
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
# Example 2:
#
# Input: nums = [-2, -1, 2, 1], k = 1
# Output: 2
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.
# Follow Up:
# Can you do it in O(n) time?


# 思路：presum list + dictionary，每次从dictionary中check的时候，都相当于check了一小节路径
from collections import defaultdict
class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre sum list
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        dic = defaultdict(int)
        dic[0] = -1
        result = 0

        for i in range(len(nums)):
            if nums[i] - k in dic:
                result = max(result, i - dic[nums[i] - k])
            if nums[i] not in dic:
                dic[nums[i]] = i
        return result

print(Solution().maxSubArrayLen([1,-1,5,-2,3], 3))