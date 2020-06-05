# 347. Top K Frequent Elements

# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]

from collections import defaultdict
from heapq import *

class Solution:
    # counting sort solution
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1

        # bucket sort, bucket的index表示有多少num出现了index次
        buckets = [None] * (len(nums) + 1)  # +1 because buckets include 0
        for key in dic.keys():
            freq = dic[key]
            if not buckets[freq]:
                buckets[freq] = [key]
            else:
                buckets[freq].append(key)

        result, i = [], len(buckets) - 1

        # find most frequent k elements from buckets
        while len(result) < k and i >= 0:
            if buckets[i]:
                result += buckets[i]
            i -= 1
        return result

    # heap solution
    def topKFrequent1(self, nums, k):
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1

        heap = []
        for key in dic.keys():
            heappush(heap, (dic[key], key))

        while len(heap) > k:  # pop out lease frequent elements
            heappop(heap)

        res = []
        while heap:
            res.append(heappop(heap)[1])
        return res
