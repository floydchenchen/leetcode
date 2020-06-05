# 22. Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution:
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""

		def backtrack(temp_list, result, open, close, n):
			if len(temp_list) == 2 * n:
				result.append("".join(temp_list))
			else:
				if open < n:
					temp_list.append("(")
					backtrack(temp_list, result, open + 1, close, n)
					temp_list.pop()
				if close < open:
					temp_list.append(")")
					backtrack(temp_list, result, open, close + 1, n)
					temp_list.pop()
		result = []
		if n <= 0:
			return result
		backtrack([], result, 0, 0, n)
		return result

sol = Solution()
sol.generateParenthesis(3)