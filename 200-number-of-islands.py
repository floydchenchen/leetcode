 # 200. Number of Islands

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3

# 经典DFS题

class Solution:
    def numIslands(self, grid):

        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                # visited
                grid[i][j] = "0"
                # map() returns an iterator, and will not process elements until you ask it to.
                # https://stackoverflow.com/questions/13623634/python-3-map-function-is-not-calling-up-function
                list(map(dfs, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))
                return 1
            return 0

        if not grid:
            return 0

        return sum([dfs(i, j) for i in range(len(grid)) for j in range(len(grid[0]))])

    def numIslands1(self, grid):
        def dfs(i, j, grid):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
                return
            grid[i][j] = "0"
            dfs(i + 1, j, grid)
            dfs(i - 1, j, grid)
            dfs(i, j + 1, grid)
            dfs(i, j - 1, grid)

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    result += 1
                    dfs(i, j, grid)
        return result




sol = Solution()
print(sol.numIslands(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
