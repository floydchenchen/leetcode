# 77. Combinations

# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# Example:
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution:
	# DFS, backtracking method
	def combine(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""

		def backtrack(n, temp_list, result, start, k):
			if len(temp_list) == k:
				result.append(list(temp_list))
			else:
				for i in range(start, n + 1):
					temp_list.append(i)
					backtrack(n, temp_list, result, i + 1, k)
					temp_list.pop()
			return result

		result = []
		if not n or not k:
			return result
		backtrack(n, [], result, 1, k)
		return result


sol = Solution()
print(sol.combine(4,2))
