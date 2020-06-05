# 719. Find K-th Smallest Pair Distance

# Given an integer array, return the k-th smallest distance among all the pairs.
# The distance of a pair (A, B) is defined as the absolute difference between A and B.
#
# Example 1:
# Input:
# nums = [1,3,1]
# k = 1
# Output: 0
# Explanation:
# Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.

# 思路：对value的binary search，找到范围内最小的value，使得有≥k个pair的distance ≤ value
class Solution:
    def smallestDistancePair(self, nums, k):

        # using sliding window to count number of pairs, assume nums is sorted
        def count_pair(nums, k, val):
            result = 0
            l, r = 0, 1
            while l < len(nums):
                while r < len(nums) and nums[r] - nums[l] <= val:
                    r += 1
                result += r - l - 1
                l += 1
            return result

        nums.sort()

        # binary search on values, 找到范围内最小值，bisect_left
        left, right = 0, nums[-1] - nums[0]
        while left <= right:
            mid = (left + right) // 2
            count = count_pair(nums, k, mid)
            if count < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

sol = Solution()
print(sol.smallestDistancePair([1,2,3], 2))