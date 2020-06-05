# 934. Shortest Bridge
# In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of
# 1s not connected to any other 1s.)
#
# Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.
#
# Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)
#
#
#
# Example 1:
#
# Input: [[0,1]
#         [1,0]]
# Output: 1
#
# Example 2:
#
# Input: [[0,1,0],
#         [0,0,0],
#         [0,0,1]]
# Output: 2
#
# Example 3:
#
# Input: [[1,1,1,1,1],
#         [1,0,0,0,1],
#         [1,0,1,0,1],
#         [1,0,0,0,1],
#         [1,1,1,1,1]]
# Output: 1
#
#
# Note:
#
# 1 <= A.length = A[0].length <= 100
# A[i][j] == 0 or A[i][j] == 1

class Solution:
    def shortestBridge(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        # use dfs to paint one island from "1" to "2"
        def dfs(nums, i, j):
            if 0 <= i <= len(nums) - 1 and 0 <= j <= len(nums[0]) - 1 and nums[i][j] == 1:
                nums[i][j] = 2
                dfs(nums, i + 1, j)
                dfs(nums, i - 1, j)
                dfs(nums, i, j + 1)
                dfs(nums, i, j - 1)

        first_island_found = False
        q, distance = [], 0
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                # mark the first island
                if nums[i][j] == 1 and not first_island_found:
                    dfs(nums, i, j)
                    first_island_found = True
                # add points of the second island to the queue
                if nums[i][j] == 1 and first_island_found:
                    q.append([i, j])

        # use bfs to find the shortest path
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.pop(0)
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x, y = i + dx, j + dy
                    if 0 <= x <= len(nums) - 1 and 0 <= y <= len(nums[0]) - 1 and nums[x][y] != 1:
                        if nums[x][y] == 2:
                            return distance
                        elif nums[x][y] == 0:
                            nums[x][y] = 1
                            q.append((x, y))
            distance += 1
        return -1


print(Solution().shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
