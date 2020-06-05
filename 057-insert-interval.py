# 57. Insert Interval

# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their start times.
#
# Example 1:
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        start, end = newInterval.start, newInterval.end
        result = []
        i = 0
        while i < len(intervals):
            # 如果new_start在old_end左边，说明可能有相交，只要new_end在old_start右边
            if start <= intervals[i].end:
                # old_start .. new_end, new_end在old_start右边，说明相交
                if intervals[i].start <= end:
                    start = min(start, intervals[i].start)
                    end = max(end, intervals[i].end)
                # 新插入的interval完全在intervals[i]的左边，说明已经找到插入点，直接break
                else:
                    break
            # new_start在old_end左边，说明没有相交，append intervals[i]进result即可
            else:
                result.append(intervals[i])
            i += 1


        result.append(Interval(start, end))
        result += intervals[i:]
        return result
