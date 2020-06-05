# 279. Perfect Squares
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

# use dp to store the min number of squares for each integer (please note dp[1], dp[4], dp[9] are all 1)
# dp[0] = 0
# dp[1] = dp[0] + 1 = 1
# dp[2] = dp[1] + 1 = 2
# dp[3] = dp[0] + 1 = 3
# dp[4] = min(dp[4 - 1*1], dp[4 - 2*2]) + 1
# dp[5] = min(dp[5 - 1*1], dp[5 - 2*2]) + 1
# ...
# dp[13] = min(dp[13 - 1*1], dp[13 - 2*2], dp[13 - 3*3]) + 1
#
# dp[n] = min(dp[n - i*i]) + 1,  n - i*i >=0 && i >= 1

# 思路:
# dp[i]: sum为i时最少需要几个完全平方数相加
# transition: 对所有小于i的完全平方数j*j，dp[i] = min(dp[i], 1 + dp[i - j * j])
import math
class Solution:
    # DP solution, O(n^1.5) time, O(n) space
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [math.inf] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            while i >= j * j:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]

    # BFS solution
    # https://leetcode.com/uploads/files/1467720855285-xcoqwin.png
    def numSquares_v2(self, n):
        square_list = []
        i = 1
        while i * i <= n:
            square_list.append(i * i)
            i += 1

        queue = {n}
        count = 0
        while queue:
            count += 1
            temp = set()
            for i in queue:
                for j in square_list:
                    if i == j:
                        return count
                    elif i > j:
                        temp.add(i - j)
                    else:
                        break
            queue = temp # 相当于在这里做了queue.pop()
        return count




sol = Solution()
print(sol.numSquares_v2(12))

