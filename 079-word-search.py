# 79. Word Search

# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells
# are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def dfs(board, i, j, word, index):
            # 退出条件
            if index == len(word):
                return True
            # 越界
            elif i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            # 不match
            elif board[i][j] != word[index]:
                return False
            else:
                c = board[i][j]
                board[i][j] = "#"
                result = dfs(board, i - 1, j, word, index + 1) \
                         or dfs(board, i + 1, j, word, index + 1) \
                         or dfs(board, i, j - 1, word, index + 1) \
                         or dfs(board, i, j + 1, word, index + 1)
                board[i][j] = c
                return result

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, word, 0):
                    return True
        return False
