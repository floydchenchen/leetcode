# 29. Divide Two Integers
# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.
#
# Example 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Note:
#
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem,
# assume that your function returns 231 − 1 when the division result overflows.

# 不能用 * / 和 %，不考虑除数为0
# 思路：用减法和>>
class Solution:
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        # 需要里外两个loop，用外面的loop保证divideng大于divisor，用里面的loop将temp值从divident开始，每次x2，然后保证dividend大于temp
        # 注意因为temp每次会倍增，所以需要必须要外面的loop
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

sol = Solution()
print(sol.divide(7, -3))
