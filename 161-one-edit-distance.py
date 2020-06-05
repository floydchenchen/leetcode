# 161. One Edit Distance
# Given two strings s and t, determine if they are both one edit distance apart.
#
# Note:
#
# There are 3 possiblities to satisify one edit distance apart:
#
# Insert a character into s to get t
# Delete a character from s to get t
# Replace a character of s to get t
# Example 1:
#
# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
# Example 2:
#
# Input: s = "cab", t = "ad"
# Output: false
# Explanation: We cannot get t from s by only one step.
# Example 3:
#
# Input: s = "1203", t = "1213"
# Output: true
# Explanation: We can replace '0' with '1' to get t.


# 三种操作：add, remove, change
# 思路：for-loop扫过range(min(len(s), len(t)), 如果遇到s[i] != t[i]
# 1. 如果len(s) == len(t)，那么只能edit s[i]
# 2. 如果len(s) < len(t)，那么只能 s add one char to equal t
# 3. 如果len(s) > len(t)，那么只能 s remove one char to equal t
# 最后的edge case，有可能两个string长度差一位，而且只有最后一位不同
class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                # if same length, only change is possible
                if len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                # s add one char to equal t
                elif len(s) < len(t):
                    return s[i:] == t[i+1:]
                # s remove one char to equal t
                else:
                    return s[i+1:] == t[i:]
        # 别忘了edge case
        # All previous chars are the same,
        # the only possibility is deleting the end char in the longer one of s and t
        return abs(len(s) - len(t)) == 1
