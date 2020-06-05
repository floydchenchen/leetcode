# 205. Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.
#
# Example 1:
#
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
#
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
#
# Input: s = "paper", t = "title"
# Output: true

from collections import defaultdict
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1, dic2 = defaultdict(list), defaultdict(list)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            dic1[s[i]].append(i)
            dic2[t[i]].append(i)

        # sort是因为dictionary的顺序是没有保证的
        return sorted(dic1.values()) == sorted(dic2.values())

sol = Solution()
print(sol.isIsomorphic("egg","add"))


