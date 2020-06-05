# 935. Knight Dialer
# A chess knight can move as indicated in the chess diagram below:
# https://assets.leetcode.com/uploads/2018/10/12/knight.png
# https://assets.leetcode.com/uploads/2018/10/30/keypad.png

# This time, we place our chess knight on any numbered key of a phone pad (indicated above),
# and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.
#
# Each time it lands on a key (including the initial placement of the knight),
# it presses the number of that key, pressing N digits total.
#
# How many distinct numbers can you dial in this manner?
#
# Since the answer may be large, output the answer modulo 10^9 + 7.
#
#
#
# Example 1:
#
# Input: 1
# Output: 10
# Example 2:
#
# Input: 2
# Output: 20
# Example 3:
#
# Input: 3
# Output: 46

class Solution:
    def knightDialer(self, n):
        """
        :type N: int
        :rtype: int
        """
        dic = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }

        dp = [1] * 10
        for _ in range(n - 1):
            next_dp = [0] * 10
            for i in range(10):
                for j in dic[i]:
                    next_dp[j] += dp[i]
            dp = next_dp
        return sum(dp) % (10 ** 9 + 7)


print(Solution().knightDialer(2))
