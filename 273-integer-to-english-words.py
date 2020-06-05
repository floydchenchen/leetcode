# 273. Integer to English Words
# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
#
# Example 1:
#
# Input: 123
# Output: "One Hundred Twenty Three"
# Example 2:
#
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:
#
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# Example 4:
#
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

class Solution:
	def numberToWords(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		# list的第0位注意一定需要存空的String，以满足“0”
		less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
		tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
		thousands = ["", "Thousand", "Million", "Billion"]

		# 用helper method check for hundreds, tens and ones
		def helper(num):
			if num == 0:
				return ""
			elif num < 20:
				return less_than_20[num] + " "
			elif num < 100:
				return tens[num // 10] + " " + helper(num % 10)
			else: # handle hundreds
				return less_than_20[num // 100] + " Hundred " + helper(num % 100)


		if num == 0:
			return "Zero"

		i = 0
		result = ""

		# 在主方法里面check thousands
		while num > 0:
			if num % 1000 > 0:
				result = helper(num % 1000) + thousands[i] + " " + result
			num //= 1000
			i += 1
		return result.strip()