# 564. Find the Closest Palindrome

# Given an integer n, find the closest integer (not including itself), which is a palindrome.
#
# The 'closest' is defined as absolute difference minimized between two integers.
#
# Example 1:
# Input: "123"
# Output: "121"
# Note:
# The input n is a positive integer represented by string, whose length will not exceed 18.
# If there is a tie, return the smaller one as answer.

# https://leetcode.com/problems/find-the-closest-palindrome/discuss/102391/python-simple-with-explanation
# https://leetcode.com/problems/find-the-closest-palindrome/discuss/102396/C++-short-solution-only-need-to-compare-5-numbers
class Solution:
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        # based on @awice and @o_sharp
        l = len(n)
        # with different digits width, it must be either 10...01 or 9...9
        candidates = set((str(10 ** l + 1), str(10 ** (l - 1) - 1)))
        # the closest must be in middle digit +1, 0, -1, then flip left to right
        prefix = int(n[:(l + 1)/2])
        for i in map(str, (prefix - 1, prefix, prefix + 1)):
            candidates.add(i + [i, i[:-1]][l & 1][::-1])
        candidates.discard(n)
        return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))