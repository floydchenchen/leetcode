# 132. Palindrome Partitioning II

# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# Example:
#
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

# 思路：1. dp[i]: s[:i]的最小次数的cut
# 2. transition: 如果s[l:r+1]是一个palindrome，那么dp[r + 1] = min(dp[r + 1], dp[l] + 1)
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [i for i in (range(-1, len(s)))]
        print(dp)
        for i in range(len(s)):
            # combining odd and even strings
            for (l, r) in [(i, i), (i, i + 1)]:
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    dp[r + 1] = min(dp[r + 1], dp[l] + 1)
                    l -= 1
                    r += 1
        return dp[len(s)]

sol = Solution()
print(sol.minCut("aab"))