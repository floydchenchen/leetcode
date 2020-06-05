# 344. Reverse String

# Write a function that takes a string as input and returns the string reversed.
#
# Example 1:
#
# Input: "hello"
# Output: "olleh"
# Example 2:
#
# Input: "A man, a plan, a canal: Panama"
# Output: "amanaP :lanac a ,nalp a ,nam A"

class Solution:
    # pythonic solution
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    # two pointer solution
    def reverseString1(self, s):
        if not s:
            return s
        chars = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1
        return "".join(chars)

    # recursive solution: divide and conquer
    def reverseString2(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseString2(s[l//2:]) + self.reverseString2(s[:l//2])
