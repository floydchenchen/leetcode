# 295. Find Median from Data Stream

# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
#
# For example,
# [2,3,4], the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Design a data structure that supports the following two operations:
#
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
#
#
# Example:
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2

from heapq import *

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap, self.max_heap = [], []
        # heapify(self.max_heap)
        # heapify(self.min_heap)

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heappush(self.max_heap, -num)
        heappush(self.min_heap, -heappop(self.max_heap))
        if len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]
