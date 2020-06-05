# 7. Reverse Integer

# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 注意维护sign
        if x == 0:
            return 0
        elif x < 0:
            sign = -1
        else:
            sign = 1

        result = int(str(x * sign)[::-1])
        return result * sign if result < 0x7fffffff else 0