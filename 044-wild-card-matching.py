# 44. Wildcard Matching

# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
# Example 1:
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
#
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:
#
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# Example 4:
#
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
# Example 5:
#
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false

class Solution:
    # recursion solution
    def isMatch(self, s, p):
        # edge cases: not p
        if not p:
            return s == ""
        # not s
        if not s:
            i = 0
            while i < len(p):
                if p[i] != "*":
                    return False
                i += 1
            return True

        if len(p) == 1 and p[0] == "*":
            return True

        # change all characters to lower cases:
        s, p = s.lower(), p.lower()
        # check if first character matches
        first_match = s and s[0] == p[0] or p[0] == "*" or p[0] == "?"
        if p[0] == "*" and len(p) > 1:
            return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    # dp solution
    # dp[i][j]: if s[:i+1] can match with p[:j+1]
    def isMatch1(self, s, p):
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        # "" matches ""
        dp[0][0] = True
        # other initialization
        for j in range(1, len(p) + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                else:
                    dp[i][j] = (p[j - 1] == s[i - 1] or p[j - 1] == '?') and dp[i - 1][j - 1]
        return dp[-1][-1]