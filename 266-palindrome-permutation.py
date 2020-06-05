# 266. Palindrome Permutation

# Given a string, determine if a permutation of the string could form a palindrome.
#
# Example 1:
#
# Input: "code"
# Output: false
# Example 2:
#
# Input: "aab"
# Output: true
# Example 3:
#
# Input: "carerac"
# Output: true

# 思路：看是否只有最多1个char出现了基数次

from collections import Counter
class Solution:
    def canPermutePalindrome(self, s):
        return sum(v % 2 for v in Counter(s).values()) <= 1
