# 680. Valid Palindrome II

# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                remove_j, remove_i = s[l:r], s[l + 1:r + 1]
                return remove_j == remove_j[::-1] or remove_i == remove_i[::-1]
            l, r = l + 1, r - 1
        return True

print(Solution().validPalindrome("abcdcxba"))