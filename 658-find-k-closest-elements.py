# 658. Find K Closest Elements

# Given a sorted array, two integers k and x, find the k closest elements to x in the array.
# The result should also be sorted in ascending order. If there is a tie, the smaller
# elements are always preferred.
#
# Example 1:
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# Example 2:
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]

# 1. Use python's custom sorting to sort the nums by each num's distance to x,
# if there is a tie we put smaller num before. For example,
# if we have [1,2,3,4,5], k=4, x=3, then the sorted array becomes [3,2,4,1,5].
# ==> sorted(nums, key=lambda num: (abs(num - x), num))
# 2. We return the first k elements in the sorted array in an ascending order.
# For example, the sorted array is [3,2,4,1,5], so we need to return [1,2,3,4].
# ==> sorted(sorted(nums, key=lambda num: (abs(num - x), num))[:k])
class Solution:
    # O(nlgn) solution
    def findClosestElements(self, nums, k, x):
        # return sorted(sorted(nums, key=lambda num: (abs(num - x), num))[:k])
        nums.sort(key=lambda num: (abs(num - x), num))
        return sorted(nums[:k])

    # O(lgn) solution: binary search
    def findClosestElements1(self, nums, k, x):
        left, right = 0, len(nums) - k - 1
        while left <= right:
            mid = (left + right) // 2
            # 如果nums[mid]比nums[mid+k]离x更远
            if x - nums[mid] > nums[mid + k] - x:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left:left + k]


# print(Solution().findClosestElements1([1,2,3,4,5],4,3))
print(Solution().findClosestElements1([1], 1, 1))
