# 253. Meeting Rooms II

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
# find the minimum number of conference rooms required.
#
# Example 1:
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: 1

from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        # sort intervals by starttime
        intervals.sort(key = lambda x: x[0])
        
        # push endtimes to heap
        heap = []
        heappush(heap, intervals[0][1])
        for interval in intervals[1:]:
            if interval[0] >= heap[0]:
                heappop(heap)
            heappush(heap, interval[1])
        return len(heap)