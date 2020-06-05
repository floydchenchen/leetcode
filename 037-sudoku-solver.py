# 37. Sudoku Solver

# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# Empty cells are indicated by the character '.'.

class Solution:
	def solveSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""

		# check current cell's row, column and cube does not contain num
		def is_valid(board, row, col, num):
			for i in range(9):
				# check rows and cols
				if board[i][col] == num or board[row][i] == num:
					return False
				# check cube
				cube_row, cube_col = 3 * (row // 3) + i // 3, 3 * (col // 3) + i % 3
				if board[cube_row][cube_col] == num:
					return False
			return True

		# this function checks whether the sudoku is solved by finding if the sudoku is filled up
		def find_open(board):
			for i in range(len(board)):
				for j in range(len(board[0])):
					if board[i][j] == ".":
						return i, j
			return -1, -1

		# this backtrack function is a boolean that indicates if the sudoku is solved
		def backtrack(board):
			# base/exit case
			row, col = find_open(board)
			if row == -1 and col == -1:
				return True
			for num in range(1, 10):
				str_num = str(num)
				if is_valid(board, row, col, str_num):
					board[row][col] = str_num
					if backtrack(board): # boolean backtracking method
						return True
					board[row][col] = "."
			return False

		backtrack(board)

sol = Solution()
sol.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])



