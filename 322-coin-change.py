# 322. Coin Change

# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1

# idea: to pick fewest number of coins, pick coins with larger denominations
# dp[i]: the fewest number of coins making up amount i
# transition: dp[i] = min(dp[i - coin] + 1)
import math
class Solution:
    # dp solution, O(len(coins)*amount) time, O(amount) space
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        _max = math.inf
        dp = [0] + [_max] * amount
        for i in range(1, amount + 1):
            dp[i] = min(dp[i-c] if i - c >= 0 else _max for c in coins) + 1
        # return "1" index of the array [dp[amount], -1] if dp[amount] == max else return array[0]
        # if dp[amount] == max then -1 else dp[amount]
        if dp[amount] == _max:
            return -1
        else:
            return dp[amount]
