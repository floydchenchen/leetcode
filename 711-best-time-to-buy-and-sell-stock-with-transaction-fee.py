# 714. Best Time to Buy and Sell Stock with Transaction Fee

# Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i;
# and a non-negative integer fee representing a transaction fee.
#
# You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
# You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
#
# Return the maximum profit you can make.
#
# Example 1:
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1
# Selling at prices[3] = 8
# Buying at prices[4] = 4
# Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

import math
class Solution:
	def maxProfit(self, prices, fee):
		"""
		:type prices: List[int]
		:type fee: int
		:rtype: int
		"""
		if not prices or len(prices) < 2:
			return 0
		s0, s1 = 0, -math.inf

		for price in prices:
			# fee at buying time
			s1 = max(s1, s0 - price - fee)
			s0 = max(s0, s1 + price)
		return s0
