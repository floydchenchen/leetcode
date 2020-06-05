# 207. Course Schedule

# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
# which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# Example 1:
#
# Input: 2, [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:
#
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.

# 思路: topological sort
# topological sort模板
# 1. build the graph with incoming degrees represented by am 1d array
# 2. identify vertices that have no incoming edge (there's a cycle if no such vertex exists), put it in queue
# 3. repeat step 2
class Solution:
    def canFinish(self, numCourses, prerequisites):
        degrees = [0] * numCourses
        q = []
        
        # 1. build degree map
        for pre in prerequisites:
            degrees[pre[0]] += 1
        # 2. build the queue (courses without any parent)
        for i in range(len(degrees)):
            if not degrees[i]:
                q.append(i)
        # 3. repeat step 2 in a while loop, reduce degree of a course if we see its parent
        while q:
            parent = q.pop(0)
            for pre in prerequisites:
                if parent == pre[1]:
                    degrees[pre[0]] -= 1
                    if not degrees[pre[0]]:
                        q.append(pre[0])
        
        # 4. check if all courses have empty degree/parent/prereq
        for degree in degrees:
            if degree:
                return False
        return True