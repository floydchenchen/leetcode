# 131. Palindrome Partitioning
#
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# Example:
#
# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

class Solution:
    # DFS backtracking
    def partition(self, s):
        def dfs(s, path, result):
            if not s:
                result.append(list(path))
                return
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    path.append(s[:i])
                    dfs(s[i:], path, result)
                    path.pop()

        result = []
        dfs(s, [], result)
        return result
