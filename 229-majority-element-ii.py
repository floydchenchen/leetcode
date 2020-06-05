# 229. Majority Element II

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#
# Note: The algorithm should run in linear time and in O(1) space.
#
# Example 1:
#
# Input: [3,2,3]
# Output: [3]
# Example 2:
#
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]

from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def majorityElement(self, nums):
            ctr = Counter()
            for n in nums:
                ctr[n] += 1
                # 如果counter里有3个元素，给每个元素的值-1
                # counter代表着这个数字比其他的数字多几个
                # 类似169里counter --的思想
                if len(ctr) == 3:
                    ctr -= Counter(set(ctr))
            return [n for n in ctr if nums.count(n) > len(nums) / 3]