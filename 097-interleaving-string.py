# 97. Interleaving String

# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
#
# Example 1:
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Example 2:
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# s1 and s2 are combined without change the order of an individual string

class Solution:
    # dfs solution
    # idea: for a char in s3, it could either come from s1 or s2
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        return self.dfs(s1, s2, s3, 0, 0, 0, [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)])

    def dfs(self, s1, s2, s3, i, j, k, invalid):
        # exit/base case
        if invalid[i][j]:
            return False
        if k == len(s3):
            return True
        valid = i < len(s1) and s1[i] == s3[k] and self.dfs(s1, s2, s3, i + 1, j, k + 1, invalid) or \
            j < len(s2) and s2[j] == s3[k] and self.dfs(s1, s2, s3, i, j + 1, k + 1, invalid)
        if not valid:
            invalid[i][j] = True
        return valid

    # dp solution
    # dp[i][j]: if s3[:i+j] is interleavable for s1[:i] and s2[:j]
    # DP table represents if s3 is interleaving at (i+j)th position when s1 is at ith position,
    # and s2 is at jth position. 0th position means empty string.
    def isInterleave_dp(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0: # s1 is empty
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0: # s2 is empty
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1] or dp[i][j-1] and s2[j-1] == s3[i+j-1]
        return dp[len(s1)][len(s2)]



