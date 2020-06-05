 # 130. Surrounded Regions

# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Example:
#
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:
#
# Surrounded regions shouldn't be on the border, which means that any 'O' on the border of the board are not
# flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border
# will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

class Solution:
    # BFS solution
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        q = []
        # check the border
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i in [0, len(board) - 1] or j in [0, len(board[0]) - 1]) and board[i][j] == "O":
                    q.append((i, j))

        # queue of "O" that are on the border
        while q:
            i, j = q.pop(0)
            if 0 <= i < len(board) and 0 <= j < len(board[i]) and board[i][j] == "O":
                board[i][j] = "#"
                q.append((i - 1, j))
                q.append((i + 1, j))
                q.append((i, j - 1))
                q.append((i, j + 1))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"

    # DFS solution
    def solve1(self, board):
        
        # ???1. ???????????“o”???????????"#" 
        # 2. ????matrix??"#"??"o"??"o"??“x”
        def dfs(i, j, board):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != "O":
                return
            board[i][j] = "#"
            # flood fill
            dfs(i + 1, j, board)
            dfs(i - 1, j, board)
            dfs(i, j + 1, board)
            dfs(i, j - 1, board)

        # edge case
        if not board:
            return

        # 1. ???????????“o”???????????"#" 
        # check horizontal border
        for i in [0, len(board) - 1]:
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    dfs(i, j, board)

        # check vertical border
        for j in [0, len(board[0]) - 1]:
            for i in range(1, len(board) - 1):
                if board[i][j] == "O":
                    dfs(i, j, board)

        # 2. ????matrix??"#"??"o"??"o"??“x”
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"