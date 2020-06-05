# 305. Number of Islands II

# A 2d grid map of m rows and n columns is initially filled with water.
# We may perform an addLand operation which turns the water at position (row, col) into a land.
# Given a list of positions to operate, count the number of islands after each addLand operation.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
# Example:
#
# Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
# Output: [1,1,2,3]
# Explanation:
#
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).
#
# 0 0 0
# 0 0 0
# 0 0 0
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
#
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
#
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
#
# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
#
# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# Follow up:
#
# Can you do it in time complexity O(k log mn), where k is the length of the positions?

class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parent, rank = {}, {}

        def find(x):
            return x if x == parent[x] else find(parent[x])

        # weighted quick union union
        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return 0
            if rank[x] < rank[y]:
                x, y = y, x
            parent[y] = x
            rank[x] += rank[x] == rank[y]
            return 1

        result, count = [], 0
        for i, j in positions:
            x = parent[x] = (i, j)
            rank[x] = 0
            count += 1
            for y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if y in parent:
                    count -= union(x, y)
            result.append(count)
        return result

print(Solution().numIslands2(3, 3, [[0,0], [0,1], [1,2], [2,1]]))