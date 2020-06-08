# 139. Word Break
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false

class Solution:
    # dp solution
    # dp[i]: word[:i]是否能被wordDict segmented
    # transition: dp[i] = dp[i-len(word)] and s[i-len(word):i] in wordDict
    # s[i:j]不需要考虑越界问题
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [True] + [False] * len(s)
        for i in range(1, len(s)+1):
            for word in wordDict:
                # transition function
                if word == s[i-len(word):i] and dp[i-len(word)]:
                    dp[i] = True
                    break
        return dp[-1]
