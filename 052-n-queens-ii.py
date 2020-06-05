# 52. N-Queens II

# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
#
# Example:
#
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

class Solution:
	# 我们从左往右扫（一个方向）
	def totalNQueens(self, n):
		"""
		:type n: int
		:rtype: List[List[str]]
		"""

		self.result = 0

		# 从左往右扫，所以只用check左边的columns，而不用check当前column和整个棋盘
		def is_valid(board, row, col):
			for i in range(len(board)):
				for j in range(col):
					# 检查row和两个对角线
					if board[i][j] == "Q" and (row == i or abs(row - i) == abs(col - j)):
						return False
			return True

		# 从左往右扫，所以记录col
		def backtrack(board, col):
			# base case
			if col == len(board):
				self.result += 1
			else:
				for i in range(len(board)):
					if is_valid(board, i, col):
						board[i][col] = "Q"
						backtrack(board, col + 1)
						board[i][col] = "."

		board = [["."] * n for _ in range(n)]
		backtrack(board, 0)
		return self.result
