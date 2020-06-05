# 441. Arranging Coins

# You have a total of n coins that you want to form in a staircase shape,
# where every k-th row must have exactly k coins.
#
# Given n, find the total number of full staircase rows that can be formed.
#
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
#
# Example 1:
#
# n = 5
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
#
# Because the 3rd row is incomplete, we return 2.
# Example 2:
#
# n = 8
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# Because the 4th row is incomplete, we return 3.

# 思路：找到first non-smaller n，使得(1+n)*n/2 >= k
# 所以可以将本题reduce成第二类Binary Search: 找到第一个不小于目标值的数
# Find the smallest n in [1,2, ..., k], where (1+n)*n/2 > k
class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if (mid + 1) * mid // 2 < n:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1 if left * (left + 1) // 2 > n else left
