# 50. Pow(x, n)

# Implement pow(x, n), which calculates x raised to the power n (xn).
#
# Example 1:
#
# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:
#
# Input: 2.10000, 3
# Output: 9.26100
# Example 3:
#
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

# 思路：
# recursive:
# 1. n < 0: return 1 / self.myPow(x, -n)
# 2. n % 2 != 0: return x * self.myPow(x, n - 1)
# 3. n % 2 == 0: return self.myPow(x * x, n // 2)
# iterative:
# 1. n < 0:  x = 1 / x, n *= -1
# 2. n % 2 != 0: result *= x
# 3. n % 2 == 0: x *= x n >>= 1

class Solution:
    # recursive
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:
            return x * self.myPow(x, n - 1)
        else:
            return self.myPow(x * x, n // 2)

    # iterative
    def myPow1(self, x, n):
        # convert n to positive
        if n < 0:
            x = 1 / x
            n *= -1

        result = 1
        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        return result




