# 210. Course Schedule II

# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
# which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses
# you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them.
# If it is impossible to finish all courses, return an empty array.
#
# Example 1:
#
# Input: 2, [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
#              course 0. So the correct course order is [0,1] .
# Example 2:
#
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
#              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
#              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

class Solution:
    def findOrder(self, numCourses, prerequisites):
        if not numCourses:
            return False

        # degree[course]这个course有多少prereq
        degree = [0] * numCourses
        result = list(degree)
        # the pointer of result[]
        index = 0
        queue = []

        # 把degree建好
        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            degree[course] += 1

        # 把queue建好
        for i in range(len(degree)):
            # 如果这门课没有prereq
            if not degree[i]:
                queue.append(i)
                result[index] = i
                index += 1

        while queue:
            prereq = queue.pop(0)
            for i in range(len(prerequisites)):
                if prereq == prerequisites[i][1]:
                    course = prerequisites[i][0]
                    degree[course] -= 1
                    if not degree[course]:
                        queue.append(course)
                        result[index] = course
                        index += 1

        return result if index == numCourses else []
