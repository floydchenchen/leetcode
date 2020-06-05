# 67. Add Binary

# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        i, j, _sum = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            if i >= 0:
                _sum += int(a[i])
                i -= 1
            if j >= 0:
                _sum += int(b[j])
                j -= 1
            result.append(_sum % 2)
            # carry
            _sum //= 2
        # don't forget the last carry could be 1
        if _sum:
            result.append(_sum)
        return "".join(map(str, result[::-1]))

