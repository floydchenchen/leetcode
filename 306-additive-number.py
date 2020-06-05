# 306. Additive Number

# Additive number is a string whose digits can form additive sequence.
#
# A valid additive sequence should contain at least three numbers. Except for the first two numbers,
# each subsequent number in the sequence must be the sum of the preceding two.
#
# Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.
#
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
#
# Example 1:
#
# Input: "112358"
# Output: true
# Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
#              1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# Example 2:
#
# Input: "199100199"
# Output: true
# Explanation: The additive sequence is: 1, 99, 100, 199.
#              1 + 99 = 100, 99 + 100 = 199

import itertools
class Solution:
	# try the combination for the first two number and see if the rest fit
	def isAdditiveNumber(self, num):
		"""
		:type num: str
		:rtype: bool
		"""
		for i, j in itertools.combinations(range(1, len(num)), 2):
			print(i, j)
			first, second = num[:i], num[i:j]
			# check leading zeroes, excluding 0 itself
			if first != str(int(first)) or second != str(int(second)):
				continue
			while j < len(num):
				next = str(int(first) + int(second))

				if not num.startswith(next, j):
					break

				j += len(next)
				first, second = second, next
			if j == len(num):
				return True
		return False

sol = Solution()
print(sol.isAdditiveNumber("112358"))

