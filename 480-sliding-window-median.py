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

# Two heaps (lo and hi). The size of hi, as measured by the number of valid elements it contains, is either equal to that of lo or one greater than that of lo, depending on the value of k. (This is an invariant we enforce when we add and remove elements from lo and hi). It's worth noting that by "valid" I mean elements within the current window.
# Lazy removal. I used a defaultdict to_remove to keep track of elements to be removed and their occurrances, and remove them if and only if they are at the top of either heaps.
# How to add and remove. The logic is extremely straightforward. When adding a new element, we always add to lo. If the element to be removed is in lo as well, great! We don't need to do anything because the heap sizes do not change. However, if the element to be removed happen to be in hi, we then pop an element from lo and add it to hi. Important: that element we pop is guaranteed be a valid element(!!) because otherwise it should have been removed during the previous iteration.
# Some may be worried that removing elements makes heaps imbalanced. That never happens! No matter how many elements are removed at the end of an iteration, they are invalid elements! The heap lo can contain all the invalid elements and much greater in size than hi, but still in perfect balance with hi. As long as lo and hi each contains half (or (half, half+1) when k is odd) of the elements in the current window, we say that they are balanced.
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