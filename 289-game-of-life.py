# 289. Game of Life

# According to the Wikipedia's article: "The Game of Life, also known simply as Life,
# is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules
# (taken from the above Wikipedia article):
#
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state.
# The next state is created by applying the above rules simultaneously to every cell in the current state,
# where births and deaths occur simultaneously.
#
# Example:
#
# Input:
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output:
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]

# Follow up:
#
# Could you solve it in-place? Remember that the board needs to be updated at the same time:
# You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite,
# which would cause problems when the active area encroaches the border of the array.
# How would you address these problems?


# 思路：用bit存[next state, current state]
# [2nd bit, 1st bit] = [next state, current state]
#
# - 00  dead (next) <- dead (current)
# - 01  dead (next) <- live (current)
# - 10  live (next) <- dead (current)
# - 11  live (next) <- live (current)

# Transition 01 -> 11: when board == 1 and lives >= 2 && lives <= 3.
# Transition 00 -> 10: when board == 0 and lives == 3.

import collections
class Solution:
    # infinite board solution
    # For the second follow-up question, here's a solution for an infinite board.
    # Instead of a two-dimensional array of ones and zeros, I represent the board as a set of live cell coordinates.
    def gameOfLifeInfinite(self, live):
        ctr = collections.Counter((I, J)
                                  for i, j in live
                                  for I in range(i - 1, i + 2)
                                  for J in range(j - 1, j + 2)
                                  if I != i or J != j)
        # print("ctr",ctr)
        return {ij
                for ij in ctr
                if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
        print("live", live)
        live = self.gameOfLifeInfinite(live)
        print(live)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = int((i, j) in live)

    # 普通的解法
    def gameOfLife1(self, board):
        # 注意不要让x和y越界
        def get_live_neighbors(board, i, j):
            lives = 0
            m, n = len(board), len(board[0])
            for x in range(max(i - 1, 0), min(i + 1, m - 1)):
                for y in range(max(j - 1, 0), min(j + 1, n - 1)):
                    lives += board[i][j] & 1
            # 去除自己
            lives -= board[i][j] & 1
            return lives

        if not board:
            return
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                lives = get_live_neighbors(board, i, j)
                # make the 2nd bit 1: 01 ---> 11
                if board[i][j] == 1 and 2 <= lives <= 3:
                    board[i][j] = 3
                # Make the 2nd bit 1: 00 ---> 10
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2

        # Get the 2nd state
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1


sol = Solution()
print(sol.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))