# 309. Best Time to Buy and Sell Stock with Cooldown

# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
#
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:
#
# Input: [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]


import math

class Solution:
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
		s0, s1, s2 = 0, -math.inf, 0
		for price in prices:
			# pre_s2因为s2的状态是rest了一天，所以没有随着price的改变而改变
			pre_s2 = s2
			s2 = s1 + price
			s1 = max(s1, s0 - price)
			s0 = max(s0, pre_s2)

		return max(s0, s2)