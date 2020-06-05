# 375. Guess Number Higher or Lower II

# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.
# However, when you guess a particular number x, and you guess wrong, you pay $x.
# You win the game when you guess the number I picked.
#
# Example:
#
# n = 10, I pick 8.
#
# First round:  You guess 5, I tell you that it's higher. You pay $5.
# Second round: You guess 7, I tell you that it's higher. You pay $7.
# Third round:  You guess 9, I tell you that it's lower. You pay $9.
#
# Game over. 8 is the number I picked.
#
# You end up paying $5 + $7 + $9 = $21.
# Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.

# dp[i][j]: lowest cost to guess the correct answer in the range (i, j)
# transition: dp[i][j] = min(x + max(dp[i][x - 1], dp[x + 1][j]) for x in range(i, j))
# 这里的max(dp[i][x-1], dp[x+1][j])的解释：
# whenever you choose a number, the feedback is always bad and therefore leads you to a worse sub-range.

class Solution:
    # top-down dp solution
    def getMoneyAmount(self, n):
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n, 0, -1):
            for j in range(i + 1, n + 1):
                dp[i][j] = min(x + max(dp[i][x - 1], dp[x + 1][j]) for x in range(i, j))
        return dp[1][n]


