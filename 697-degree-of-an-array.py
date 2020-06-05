# 697. Degree of an Array

# Given a non-empty array of non-negative integers nums, the degree of this array is defined as
# the maximum frequency of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums,
# that has the same degree as nums.
#
# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6

from collections import Counter, defaultdict
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        degree = max(counter.values())
        dic = defaultdict(list)
        for i, num in enumerate(nums):
            dic[num].append(i)
        return min(dic[key][-1] - dic[key][0] + 1 for key in dic.keys() if counter[key] == degree)
