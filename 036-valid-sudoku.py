# 36. Valid Sudoku

# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the
# following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
# Example 1:
#
# Input:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
# Example 2:
#
# Input:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being
#     modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

class Solution:
    # 思路比较简单的版本
    def isValidSudoku(self, board):
        def is_row_valid(board):
            for row in board:
                if not is_unit_valid(row):
                    return False
            return True

        def is_col_valid(board):
            for col in zip(*board):
                if not is_unit_valid(col):
                    return False
            return True

        def is_cube_valid(board):
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    cube = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                    if not is_unit_valid(cube):
                        return False
            return True

        def is_unit_valid(unit):
            unit = [i for i in unit if i != '.']
            return len(set(unit)) == len(unit)

        return (is_row_valid(board) and
                is_col_valid(board) and
                is_cube_valid(board))

    # one pass 版本, three sets
    def isValidSudoku1(self, board):
        for i in range(len(board)):
            rows, cols, cubes = set(), set(), set()
            for j in range(len(board[0])):
                if board[i][j] != "." and board[i][j] in rows:
                    return False
                else:
                    rows.add(board[i][j])
                if board[j][i] != "." and board[j][i] in cols:
                    return False
                else:
                    cols.add(board[j][i])
                # 用倍数控制row，用余数控制col
                cube_row, cube_col = 3 * (i // 3) + j // 3, 3 * (i % 3) + j % 3
                if board[cube_row][cube_col] != "." and board[cube_row][cube_col] in cubes:
                    return False
                else:
                    cubes.add(board[cube_row][cube_col])
        return True

