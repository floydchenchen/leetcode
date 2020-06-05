# 630. Course Schedule III
# There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and closed on dth day. 
# A course should be taken continuously for t days and must be finished before or on the dth day. You will start at the 1st day.

# Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.

# Example:

# Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
# Output: 3
# Explanation: 
# There're totally 4 courses, but you can take 3 courses at most:
# First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
# Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
# Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
# The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.

import heapq
class Solution:
    # greedy heap solution
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # sort courses by end time
        courses.sort(key = lambda c: c[1])
        print(courses)
        heap, sum_time = [], 0
        for time, end in courses:
            # max heap for time
            heapq.heappush(heap, -time)
            sum_time += time
            # if cur time is before end time of the course, unlearn the course that takes the longest time.
            if sum_time > end:
                sum_time += heapq.heappop(heap)
        return len(heap)