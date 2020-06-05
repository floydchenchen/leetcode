# 772. Basic Calculator III

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -,
# non-negative integers and empty spaces .
#
# The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses )
# and empty spaces . The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid. All intermediate results will be in the
# range of [-2147483648, 2147483647].
#
# Some examples:
#
# "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12

class Solution:
	def calculate(self, s: str) -> int:

		# first define a couple helper methods

		# operation helper to perform basic math operations
		def operation(op: str, second: int, first: int) -> int:
			if op == "+":
				return first + second
			elif op == "-":
				return first - second
			elif op == "*":
				return first * second
			elif op == "/":  # integer division
				return first // second

		# calculate the relative precedence of the the operators "*/" > "+=" > "()"
		# and determine if we want to do a pre-calculation in the stack
		# (when current_op is <= op_from_ops)
		def precedence(c: str) -> bool:
			if c in '+-': 
				return 1
			if c in '*/': 
				return 2
			return 0

		if not s:
			return 0
		# define two stack: nums to store the numbers and ops to store the operators
		nums, ops = [], []
		ops_set = {"+", "-", "*", "/"}
		i = 0
		# add a prev variable to deal negative numbers:
		prev = False
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
				prev = True
				nums.append(num)
			elif c == "(":
				ops.append(c)
				prev = False
			elif c == ")":
				# do the math when we encounter a ')' until '('
				while ops[-1] != "(":
					nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
				ops.pop()
			elif c in ops_set:
				# handle negative number
				if not prev:
					nums.append(0)
				# do pre-calc when current_op is <= op_from_ops
				while ops and precedence(ops[-1]) >= precedence(c):
					nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
				ops.append(c)
			i += 1

		while ops:
			nums.append(operation(ops.pop(), nums.pop(), nums.pop()))

		return nums.pop()




sol = Solution()
print(sol.calculate(" 2-1 + 2 "))
