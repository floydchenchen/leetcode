# 231. Power of Two
# Given an integer, write a function to determine if it is a power of two.

# Example 1:

# Input: 1
# Output: true 
# Explanation: 20 = 1
# Example 2:

# Input: 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: 218
# Output: false

class Solution:
    # 看二进制是否只有最高位是1，其余全部是0
    # e.g. 1000 & 0111 = 0
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return not n & (n - 1)