# 150. Evaluate Reverse Polish Notation

# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Note:
#
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would always evaluate to a
# result and there won't be any divide by zero operation.
# Example 1:
#
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:
#
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:
#
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation:
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

class Solution:
	def evalRPN(self, tokens):
		"""
		:type tokens: 1List[str]
		:rtype: int
		"""

		def operation(op, second, first):
			if op == "*":
				return first * second
			elif op == "/":
				# since python // is different than java /: python always does floor division
				# https://stackoverflow.com/questions/5535206/negative-integer-division-surprising-result
				return int(first / second)
			elif op == "+":
				return first + second
			else:
				return first - second

		result = []
		for token in tokens:
			if token.lstrip("-").isdigit():
				result.append(int(token))
			else:
				result.append(operation(token, result.pop(), result.pop()))
		return result.pop()

sol = Solution()
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
