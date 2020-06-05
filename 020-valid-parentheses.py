# 20. Valid Parentheses

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true

class Solution:
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		# edge cases: 如果长度为奇数，直接返回False
		if not s:
			return True
		elif len(s) % 2 == 1:
			return False
		# 用dictionary减少各种if比较次数
		dic = {"(": ")", "[": "]", "{": "}"}
		stack = []
		for c in s:
			if c in dic:
				stack.append(dic[c])
			elif not stack or stack.pop() != c:
				return False
		return not stack

sol = Solution()
print(sol.isValid("()"))