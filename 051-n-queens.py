# 51. N-Queens

# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both
# indicate a queen and an empty space respectively.
#
# Example:
#
# Input: 4
# Output: [
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
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.


class Solution:
	# 我们从左往右扫（一个方向）
	def solveNQueens(self, n):
		"""
		:type n: int
		:rtype: List[List[str]]
		"""

		# 从左往右扫，所以只用check左边的columns，而不用check当前column和整个棋盘
		def is_valid(board, row, col):
			for i in range(len(board)):
				for j in range(col):
					# 检查row和两个对角线
					if board[i][j] == "Q" and (row == i or abs(row - i) == abs(col - j)):
						return False
			return True

		def construct_board(board):
			result = []
			for entire_row in board:
				result.append("".join(entire_row))
			return result

		# 从左往右扫，所以记录col
		def backtrack(board, col, result):
			# base case
			if col == len(board):
				result.append(construct_board(board))
			else:
				for i in range(len(board)):
					if is_valid(board, i, col):
						board[i][col] = "Q"
						backtrack(board, col + 1, result)
						board[i][col] = "."

		result = []
		board = [["."] * n for _ in range(n)]
		backtrack(board, 0, result)
		return result

sol = Solution()
print(sol.solveNQueens(4))