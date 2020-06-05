# 201. Bitwise AND of Numbers Range

# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
#
# Example 1:
#
# Input: [5,7]
# Output: 4
# Example 2:
#
# Input: [0,1]
# Output: 0
class Solution:
    # solution 1
    def rangeBitwiseAnd(self, m, n):
        while m < n:
            n = n & (n-1)
        return n

    # solution 2
    def rangeBitwiseAnd1(self, m, n):
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i