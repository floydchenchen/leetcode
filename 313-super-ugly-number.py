# 313. Super Ugly Number

# Write a program to find the nth super ugly number.
#
# Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.
#
# Example:
#
# Input: n = 12, primes = [2,7,13,19]
# Output: 32
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12
#              super ugly numbers given primes = [2,7,13,19] of size 4.
# Note:
#
# 1 is a super ugly number for any given primes.
# The given numbers in primes are in ascending order.
# 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

# 思路：each new ugly number is generated from the previous ugly number by multiplying one of the prime
from heapq import *
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        heap, result = [], [1]
        for i in range(len(primes)):
            heappush(heap, (primes[i], 0, primes[i]))
        while len(result) < n:
            num, i, prime = heap[0]
            result.append(num)
            while heap and heap[0][0] == num:
                num, i, prime = heappop(heap)
                heappush(heap, (prime * result[i + 1], i + 1, prime))
        return result[-1]

print(Solution().nthSuperUglyNumber(5, [2,7,13,19]))