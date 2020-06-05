# 410. Split Array Largest Sum

# Given an array which consists of non-negative integers and an integer m,
# you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.
#
# Note:
# If n is the length of array, assume the following constraints are satisfied:
#
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# Examples:
#
# Input:
# nums = [7,2,5,10,8]
# m = 2
#
# Output:
# 18
#
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.

# 思路：binary search，对value的binary search，找到范围内一个最小的value，使得value为满足：
# 将nums分为m个subarray，使得每个subarray的值都小于value
# 1. 对value而不会是index的binary search
# 2. 找到第一个不小于目标值的数(第二类binary search) ==> return left
# 3. 用子函数当作判断关系（第四类binary search）
class Solution:
    def splitArray(self, nums, m):
        # 是否能将nums分为m个subarray，使得每个subarray的值都小于value
        def valid(nums, m, value):
            count, _sum = 1, 0
            for num in nums:
                _sum += num
                if _sum > value:
                    count += 1
                    _sum = num
                    if count > m:
                        return False
            return True

        # binary search on value
        if m == 1:
            return sum(nums)
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if valid(nums, m, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

print(Solution().splitArray([7,2,5,10,8], 2))
