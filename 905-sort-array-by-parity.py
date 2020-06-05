# 905. Sort Array By Parity
# Given an array A of non-negative integers, return an array consisting of all the even elements of A,
# followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # even and orr pointers for the array
        l, r = 0, len(A) - 1
        while l < r:
            while A[l] % 2 == 0 and l < r:
                l += 1
            while A[r] % 2 == 1 and l < r:
                r -= 1
            A[l], A[r] = A[r], A[l]
        return A