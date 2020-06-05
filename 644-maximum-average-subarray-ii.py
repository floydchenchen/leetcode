# 644. Maximum Average Subarray II

# Given an array consisting of n integers, find the contiguous subarray
# whose length is greater than or equal to k that has the maximum average value.
# And you need to output the maximum average value.
#
# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation:
# when length is 5, maximum average value is 10.8,
# when length is 6, maximum average value is 9.16667.
# Thus return 12.75.

# Note:
# 1 <= k <= n <= 10,000.
# Elements of the given array will be in range [-10,000, 10,000].
# The answer with the calculation error less than 10-5 will be accepted.


# 思路：对value的binary search，找到范围内最小的value，使得所有长度 >= k的subarray的均值都 <= value
# bisect_right + 自定义函数做判断
# 所有不用built-in function的python解法本题全部超时

class Solution:
    def findMaxAverage(self, nums, k):

        # 自定义函数：是否能找到长度 >= k的subarray，使得subarray的均值 > value
        # 先将所有元素减mid，再找sum有没有大于0
        def check(mid):
            _sum = 0
            for i in range(k):
                _sum += nums[i] - mid
            if _sum >= 0:
                return True
            prev = 0
            min_sum = 0
            for i in range(k, len(nums)):
                _sum += nums[i] - mid
                prev += nums[i-k] - mid
                min_sum = min(min_sum, prev)
                if _sum >= min_sum:
                    return True
            return False

        left, right = min(nums), max(nums)
        precision = 1E-6
        while left + precision < right:
            mid = (left + right) / 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left

sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))