# 17. Letter Combinations of a Phone Number

# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.
#
# A dicping of digit to letters (just like on the telephone buttons) is given below.
# Note that 1 does not dic to any letters.
#
#
#
# Example:
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution:
	# BFS solution using a queue
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		dic, q = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"], []
		if len(digits) == 0 or not digits:
			return q

		q.append("")  # dummy in the queue for pop, important in this method
		for i in range(len(digits)):
			# 先把dic_index从s听变成integer
			dic_index = int(digits[i])
			# 当q的第一个的长度还是目前i的长度，说明它还要增加它的长度
			while len(q[0]) == i:
				temp = q.pop(0)
				# e.g., temp = "a", dic[dic_index] = "def", 往q里分别加"ad", "ae", "af"
				for c in dic[dic_index]:
					q.append(temp + c)
		return q

	# BFS solution without using a queue
	def letterCombinations_1(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		dic = {
			"2": "abc",
			"3": "def",
			"4": "ghi",
			"5": "jkl",
			"6": "mno",
			"7": "pqrs",
			"8": "tuv",
			"9": "wxyz"
		}
		result = []
		if len(digits) == 0 or not digits:
			return result

		result.append("")
		for digit in digits:
			temp = []
			for c in dic[digit]:
				for combination in result:
					temp.append(combination + c)
			result = temp
		return result

	# backtracking solution / DFS solution
	def letterCombinations_2(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		dic = {
			"2": "abc",
			"3": "def",
			"4": "ghi",
			"5": "jkl",
			"6": "mno",
			"7": "pqrs",
			"8": "tuv",
			"9": "wxyz"
		}


		def backtracking(i, char_arr, result):
			if i == len:
				result.append("".join(char_arr))
			else:
				for c in dic[digits[i]]:
					char_arr.append(c)
					backtracking(i + 1, char_arr, result)
					char_arr.pop()

		result = []
		# edge case
		if len(digits) == 0 or not digits:
			return result
		backtracking(0, [], result)
		return result

sol = Solution()
print(sol.letterCombinations_2("23"))

