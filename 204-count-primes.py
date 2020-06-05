# 204. Count Primes

# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [False] * 2 + [True] * (n - 2)
        i = 2
        # 只需要检查到 sqrt(n)即可
        while i * i <= n:
            if primes[i]:
                # 骚方法
                primes[i+i:n:i] = [False] * len(primes[i+i:n:i])
                print(primes)
            i += 1
        return sum(primes)


sol = Solution()
print(sol.countPrimes(10))