# 694. Number of Distinct Islands

# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally 
# (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated 
# (and not rotated or reflected) to equal the other.

# Example 1:
# 11000
# 11000
# 00011
# 00011
# Given the above grid map, return 1.
# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.

# Notice that:
# 11
# 1
# and
#  1
# 11
# are considered different island shapes, because we do not consider reflection / rotation.

class Solution:
    # 思路，用路径来判断是否是一个island是否是一个distinct island
    # 不会出现一个岛屿不同路径的情况，因为dfs有先后顺序，同时visited position会被marked off
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        def dfs(i: int, j: int, path: List[str], direction: str) -> None:
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]:
                # mark off current position
                grid[i][j] = 0
                path.append(direction)
                # up, down, left and right
                for x, y, d in [(-1 ,0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")]:
                    dfs(i+x, j+y, path, d)
                path.append("b") # back

        
        # storing different paths marking dinstinct islands
        islands = set()
        if not grid:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    path = []
                    dfs(i, j, path, "o") # origin
                    if path:
                        islands.add("".join(path))
        return len(islands)