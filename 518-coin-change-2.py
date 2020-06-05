# 518. Coin Change 2

# You are given coins of different denominations and a total amount of money. 
# Write a function to compute the number of combinations that make up that amount. 
# You may assume that you have infinite number of each kind of coin.

 

# Example 1:

# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:

# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# Example 3:

# Input: amount = 10, coins = [10] 
# Output: 1

class Solution:
    # 将问题转化为DP的背包问题：有一个背包，最大容量为amount，每个物品的重量为coins[i]，每个物品的数量无限。有多少种方法，能够把背包恰好装满？
    # dp[i][j]: 对前i个物品，有几种方式恰好能装到容量为j的包
    # initial: dp[i][0] = 1
    # transition: dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [([1] + [0] * amount) for _ in range(n + 1)]
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if j - coins[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        return dp[n][amount]

