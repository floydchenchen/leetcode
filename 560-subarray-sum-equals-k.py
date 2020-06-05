# 560. Subarray Sum Equals K

# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:

# Input:nums = [1,1,1], k = 2
# Output: 2
 
from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # If k == 0, then search for any consecutive pair of 0s.
        if k == 0:
            return any(nums[i] == 0 and nums[i + 1] == 0 for i in range(len(nums) - 1))
        # cur_sum mod by k
        mods_dic, cum_sum = {0: -1}, 0
        #  we will keep track of indices of the cumulative sum (or prefix sum) mod by k in a dictionary mods_dic. 
        #  We will return True if we've seen a cumulative sum % k at least 2 indices before.
        for i, n in enumerate(nums):
            cum_sum = (cum_sum + n) % k
            if cum_sum in mods_dic and i - mods_dic[cum_sum] > 1:
                return True
            if cum_sum not in mods_dic:
                mods_dic[cum_sum] = i
        return False

sol = Solution()
print(sol.checkSubarraySum([23, 2, 4, 6, 7], 6))