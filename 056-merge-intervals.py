# 56. Merge Intervals
# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

# 思路：Just go through the intervals sorted by start coordinate.
# Either combine the current interval with the previous one if they overlap,
# or add it to the output by itself if they don't.

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        # sort intervals by start time
        for interval in sorted(intervals, key=lambda i: i.start):
            # 如果新的interval的start time <= 之前的intervals最后的end time: merge interval
            if result and interval.start <= result[-1].end:
                result[-1].end = max(result[-1].end, interval.end)
            else:
                result.append(interval)
        return result
