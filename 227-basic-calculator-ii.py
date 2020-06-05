# 227. Basic Calculator II

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
# The integer division should truncate toward zero.
#
# Example 1:
#
# Input: "3+2*2"
# Output: 7
# Example 2:
#
# Input: " 3/2 "
# Output: 1
# Example 3:
#
# Input: " 3+5 / 2 "
# Output: 5

class Solution:
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		# first define a couple helper methods

		# operation helper to perform basic math operations
		def operation(op, second, first):
			if op == "+":
				return first + second
			elif op == "-":
				return first - second
			elif op == "*":
				return first * second
			elif op == "/": # integer division
				return first // second

		# calculate the relative precedence of the the operators "()" > "*/" > "+="
		# and determine if we want to do a pre-calculation in the stack
		# (when current_op is <= op_from_ops)
		def precedence(current_op, op_from_ops):
			if (current_op == "*" or current_op == "/") and (op_from_ops == "+" or op_from_ops == "-"):
				return False
			return True

		if not s:
			return 0
		# define two stack: nums to store the numbers and ops to store the operators
		nums, ops = [], []
		i = 0
		while i < len(s):
			c = s[i]
			if c == " ":
				i += 1
				continue
			elif c.isdigit():
				num = int(c)
				while i < len(s) - 1 and s[i+1].isdigit():
					num = num * 10 + int(s[i+1])
					i += 1
				nums.append(num)
			elif c in ["+", "-", "*", "/"]:
				while len(ops) != 0 and precedence(c, ops[-1]):
					nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
				ops.append(c)
			i += 1

		while len(ops) > 0:
			nums.append(operation(ops.pop(), nums.pop(), nums.pop()))

		return nums.pop()

sol = Solution()
print(sol.calculate(" 3+5 / 2 "))
