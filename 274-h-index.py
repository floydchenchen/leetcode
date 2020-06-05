# 274. H-Index

# Given an array of citations (each citation is a non-negative integer) of a researcher,
# write a function to compute the researcher's h-index.
#
# According to the definition of h-index on Wikipedia:
# "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers
# have no more than h citations each."
#
# Example:
#
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
#              received 3, 0, 6, 1, 5 citations respectively.
#              Since the researcher has 3 papers with at least 3 citations each and the remaining
#              two with no more than 3 citations each, her h-index is 3.

# 思路：bucket sort
class Solution:
    def hIndex(self, nums):
        """
        :type citations: List[int]
        :rtype: int
        """
        # edge case
        if len(nums) == 0:
            return 0
        # 先找最大值，再根据0~_max来建bucket
        _max = max(nums)
        buckets = [0] * (_max + 1)
        for num in nums:
            buckets[num] += 1
        accum = 0
        for i in range(len(buckets) - 1, -1, -1):
            buckets[i] += accum
            accum = buckets[i]
            if buckets[i] >= i:
                return i
        return 0
