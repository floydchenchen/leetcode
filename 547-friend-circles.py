# 547. Friend Circles
# There are N students in a class. Some of them are friends, while some are not.
# Their friendship is transitive in nature. For example, if A is a direct friend of B,
# and B is a direct friend of C, then A is an indirect friend of C.
# And we defined a friend circle is a group of students who are direct or indirect friends.
#
# Given a N*N matrix M representing the friend relationship between students in the class.
# If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.
# And you have to output the total number of friend circles among all the students.
#
# Example 1:
# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.
# Example 2:
# Input:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

# 这个题和the number of islands题的区别：
# The members of a circle need not be all connected unlike in an "island", for e.g,
#
# [1,1,0,0,1]
# [1,1,0,0,0]
# [0,0,1,1,0]
# [0,0,1,1,0]
# [1,0,0,0,1]

# 0和5是connected，但是"地理上"并没有

class Solution:
    # dfs solution
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        def dfs(M, visited, i):
            for j in range(len(M)):
                if M[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    print(visited)
                    dfs(M, visited, j)

        visited = [False] * len(M)
        result = 0
        for i in range(len(M)):
            if not visited[i]:
                dfs(M, visited, i)
                result += 1
        return result


    # union find solution, exceeds time limit
    def findCircleNum1(self, M):

        def find(i):
            root = i
            # find the root
            while root != roots[root]:
                root = roots[root]
            # change the root of (all nodes that are connected to i) to root
            while i != root:
                temp_i = roots[i]
                roots[i] = root
                i = temp_i
            return i

        def union(i, j):
            root_i, root_j = find(i), find(j)
            if root_i == root_j:
                return 0
            if size[root_i] < size[root_j]:
                roots[root_i] = root_j
                size[root_j] += size[root_i]
            else:
                roots[root_j] = root_i
                size[root_i] += size[root_j]
            return 1

        m = len(M)
        if not M:
            return 0

        roots = [i for i in range(m)]
        size = [1] * m
        count = m

        for i in range(m):
            for j in range(i+1, m):
                if M[i][j] == 1:
                    count -= union(i, j)
                    print(roots)
        return count





# M = [[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]
# M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
M = [[1,1,1],[1,1,1],[1,1,1]]
sol = Solution()
print(sol.findCircleNum1(M))