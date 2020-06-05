# 224. Basic Calculator
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers
# and empty spaces .
#
# Example 1:
#
# Input: "1 + 1"
# Output: 2
# Example 2:
#
# Input: " 2-1 + 2 "
# Output: 3
# Example 3:
#
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23

class Solution:
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		# helper methods

		# operate helper to perform basic math operations
		def operate(op, second, first):
			if op == "+":
				return first + second
			elif op == "-":
				return first - second

		# calculate the relative precedence of the the operators "()" > "+="
		# and determine if we want to do a pre-calculation in the stack
		# (if current_op is <= op_from_ops)
		def should_pre_calc(current_op, op_from_ops):
			if op_from_ops == "(" or op_from_ops == ")":
				return False
			# if (current_op == "*" or current_op == "/") and (op_from_ops == "+" or op_from_ops == "-"):
			# 	return False
			return True


		# edge case
		if not s:
			return 0

		# two stacks: nums: numbers; ops: operators
		nums, ops = [], []
		i = 0
		while i < len(s):
			c = s[i]
			if c == " ":
				i += 1
				continue
			elif c.isdigit():
				num = int(c)
				while i < len(s) - 1 and s[i + 1].isdigit():
					num = num * 10 + int(s[i + 1])
					i += 1
				nums.append(num)
			elif c == "(":
				ops.append(c)
			elif c == ")":
				while ops[-1] != "(":
					nums.append(operate(ops.pop(), nums.pop(), nums.pop()))
				ops.pop()
			elif c in ["+", "-"]:
				while ops and should_pre_calc(c, ops[-1]):
					nums.append(operate(ops.pop(), nums.pop(), nums.pop()))
				ops.append(c)
			i += 1

		while ops:
			nums.append(operate(ops.pop(), nums.pop(), nums.pop()))

		return nums.pop()

sol = Solution()
print(sol.calculate("1 + 1"))