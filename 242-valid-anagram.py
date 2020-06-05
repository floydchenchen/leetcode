# 242. Valid Anagram

# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false

from collections import defaultdict
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1, dic2 = defaultdict(int), defaultdict(int)
        for c in s:
            dic1[c] += 1
        for c in t:
            dic2[c] += 1
        return dic1 == dic2