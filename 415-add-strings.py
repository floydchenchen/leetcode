# 415. Add Strings

# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # two pointer methods，常规的从右往左相加
        i, j = len(num1) - 1, len(num2) - 1
        _sum, result = 0, ""
        # 这个 while _sum就可以省去最后一步检查最后的可能多出来的一个1
        while _sum or i >= 0 or j >= 0:
            digit1 = int(num1[i]) if i > -1 else 0
            digit2 = int(num2[j]) if j > -1 else 0

            _sum += digit1 + digit2
            result = str(_sum % 10) + result

            _sum //= 10
            i -= 1
            j -= 1
        return result
