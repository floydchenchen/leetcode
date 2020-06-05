# 523. Continuous Subarray Sum

# Given a list of non-negative numbers and a target integer k, write a function 
# to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, 
# that is, sums up to n*k where n is also an integer.

# Example 1:

# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
# Example 2:

# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # check if there are continuous element equaling 0
        if k == 0:
            return any(nums[i] == 0 and nums[i + 1] == 0 for i in range(len(nums) - 1))
        # dic中存 presum mod k的值的index
        dic, sum_mod_k = {0: -1}, 0
        for i, num in enumerate(nums):
            # presum mod k
            sum_mod_k = (sum_mod_k + num) % k
            # 如果presum值在dic中而且长度大于1
            if sum_mod_k in dic and i - dic[sum_mod_k] > 1:
                return True
            if sum_mod_k not in dic:
                dic[sum_mod_k] = i
        return False

sol = Solution()
print(sol.checkSubarraySum([23, 2, 4, 6, 7], 6))