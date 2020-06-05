# 338. Counting Bits

# Given a non negative integer number num. For every numbers i in the range 0 ¡Ü i ¡Ü num calculate the number of 1's in their binary representation and return them as an array.

# Example 1:

# Input: 2
# Output: [0,1,1]
# Example 2:

# Input: 5
# Output: [0,1,1,2,1,2]

class Solution:
    def countBits(self, num: int) -> List[int]:
        memo = [0] * (num + 1)
        offset = 1
        for i in range(1, num + 1):
            if offset * 2 == i:
                offset *= 2
            # the core function
            memo[i] = memo[i - offset] + 1
        return memo