# 91. Decode Ways

# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# dp[i] s[:i]有几种decode的方式
# transition: dp[i] += dp[i-1] (if 'x') or += d[i-2] (if 'xy')
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # XY可以解码的条件是：9 < XY <= 26
        # X可以单独解码的条件是：X != '0'
        if not s or s[0] == "0":
            return 0
        n = len(s)
        # includes one more ""
        dp = [0] * (n + 1)
        # # "" has one way to be decoded
        dp[0] = 1
        # 0 has 0 way to encode
        dp[1] = 0 if s[0] == "0" else 1
        for i in range(2, n + 1):
            x = int(s[i-1:i])
            xy = int(s[i-2:i])
            if x:
                dp[i] += dp[i-1]
            if 10 <= xy <=26:
                dp[i] += dp[i-2]
        return dp[n]