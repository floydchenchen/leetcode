# 214. Shortest Palindrome

# Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it.
# Find and return the shortest palindrome you can find by performing this transformation.
#
# Example 1:
#
# Input: "aacecaaa"
# Output: "aaacecaaa"
# Example 2:
#
# Input: "abcd"
# Output: "dcbabcd"

class Solution:
    # brute force
    def shortestPalindrome(self, s):
        if not s:
            return s
        r = s[::-1]
        for i in range(len(s)):
            if s.startswith(r[i:]):
                return r[:i] + s

    # two pointer + recursion
    # i从左往右，j从右往左，i能表示目前s[:i]有可能是左边最长的一个palindrome
    # 例如"babcd": i = 3, s[:i] = bab; dbabcde: i = 4, s[:i] = dbab，是假的palindrome
    # 所以需要return s[i:][::-1] + self.shortestPalindrome1(s[:i]) + s[i:]
    def shortestPalindrome1(self, s):
        i = 0
        for j in range(len(s) - 1, -1, -1):
            if s[i] == s[j]:
                i += 1
        if i == len(s):
            return s
        return s[i:][::-1] + self.shortestPalindrome1(s[:i]) + s[i:]

print(Solution().shortestPalindrome1("babcd"))
