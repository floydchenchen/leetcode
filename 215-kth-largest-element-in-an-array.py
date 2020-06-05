# 215. Kth Largest Element in an Array
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
# not the kth distinct element.
#
# Example 1:
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4

import math
from heapq import *

class Solution:
    # quick-select method (similar to quick-sort)
    def quick_select(self, nums, start, end, k):
        if start > end:
            return math.inf
        pivot = nums[end]
        pivot_index = start
        for i in range(start, end):
            # put numbers < pivot to pivot's left partition
            if nums[i] <= pivot:
                # swap
                nums[pivot_index], nums[i] = nums[i], nums[pivot_index]
                pivot_index += 1

        # finally, swap A[end] with A[pivot_index], to place the pivot in the middle
        nums[pivot_index], nums[end] = nums[end], nums[pivot_index]

        # if found kth smallest number
        if pivot_index == k:
            return nums[pivot_index]
        # check right partition
        elif pivot_index < k:
            return self.quick_select(nums, pivot_index + 1, end, k)
        # check left partition
        else:
            return self.quick_select(nums, start, pivot_index - 1, k)

    # quick-select solution
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return math.inf
        return self.quick_select(nums, 0, len(nums) - 1, len(nums) - k)

    # heap solution
    def findKthLargest1(self, nums, k):
        heap = []
        for num in nums:
            heappush(heap, num)
        for _ in range(len(nums) - k):
            heappop(heap)
        return heappop(heap)
