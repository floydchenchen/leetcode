# 159. Longest Substring with At Most Two Distinct Characters
# Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.
#
# Example 1:
#
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
# Example 2:
#
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.

class Solution:
    # map solution + sliding window
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        left, result = 0, 0
        for i, c in enumerate(s):
            dic[c] = i
            if len(dic) > 2:
                left = min(dic.values())
                del dic[s[left]]
                left += 1
            result = max(result, i - left + 1)
        return result