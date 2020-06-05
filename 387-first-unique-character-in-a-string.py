# 387. First Unique Character in a String

# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.

from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)
        # print(counter)
        for i in range(len(s)):
            c = s[i]
            if counter[c] == 1:
                return i
        return -1

sol = Solution()
print(sol.firstUniqChar("loveleetcode"))