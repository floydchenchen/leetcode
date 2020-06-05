# 994. Rotting Oranges
# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

# https://assets.leetcode.com/uploads/2019/02/16/oranges.png

class Solution:
    # BFS
    # 1. 注意考虑几个edge case，如果完全没有rotten和全部都是rotten
    # 2. BFS的时候注意边界
    # 3. 注意最后是否所有的fresh全部清零
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, count, q = 0, 0, []
        if not grid:
            return count
        # put all rotten oranges in the queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        while q:
            level_length = len(q)
            for _ in range(level_length):
                cell = q.pop(0)
                i, j = cell
                for x, y in [(-1 ,0), (1, 0), (0, -1), (0, 1)]:
                    if 0<= i+x < len(grid) and 0 <= j+y < len(grid[0]) and grid[i+x][j+y] == 1:
                        q.append((i+x, j+y))
                        grid[i+x][j+y] = 2
                        fresh -= 1
            if q:
                count += 1
        
        return  count if fresh == 0 else -1