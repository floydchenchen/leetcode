# 480. Sliding Window Median

# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. 
# So the median is the mean of the two middle value.

# Examples:
# [2,3,4] , the median is 3

# [2,3], the median is (2 + 3) / 2 = 2.5

# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
# You can only see the k numbers in the window. Each time the sliding window moves right by one position. 
# Your job is to output the median array for each window in the original array.

# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

# Window position                Median
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7       3
#  1  3  -1  -3 [5  3  6] 7       5
#  1  3  -1  -3  5 [3  6  7]      6
# Therefore, return the median sliding window as [1,-1,-1,3,5,6].
from collections import defaultdict
from heapq import *
class Solution:
    def medianSlidingWindow(self, nums, k):
        if not nums or not k:
            return []
        max_heap = [] # lower half max heap
        min_heap = [] # upper half min heap
        
        # deal with the first window 
        for i in range(k):
            if len(max_heap) == len(min_heap):
                heappush(min_heap, -heappushpop(max_heap, -nums[i]))
            else:
                heappush(max_heap, -heappushpop(min_heap, nums[i]))
        # k & 1: k is odd
        result = [float(min_heap[0])] if k & 1 else [(min_heap[0] - max_heap[0]) / 2.0]
        # use a map to lazily remove element outside left boundary
        to_remove = defaultdict(int)
        # right bound of window
        for r in range(k, len(nums)):
            # always push to max_heap first
            heappush(max_heap, -heappushpop(min_heap, nums[r]))
            # the number to be out
            out_num = nums[r-k]
            if out_num > -max_heap[0]:
                heappush(min_heap, -heappop(max_heap))
            to_remove[out_num] += 1
            while max_heap and to_remove[-max_heap[0]]:
                to_remove[-max_heap[0]] -= 1
                heappop(max_heap)
            while to_remove[min_heap[0]]:
                to_remove[min_heap[0]] -= 1
                heappop(min_heap)
            if k % 2:
                result.append(float(min_heap[0]))
            else:
                result.append((min_heap[0] - max_heap[0]) / 2.0)
        return result

sol = Solution()
print(sol.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))