# 887. Super Egg Drop

# You are given K eggs, and you have access to a building with N floors from 1 to N. 

# Each egg is identical in function, and if an egg breaks, you cannot drop it again.

# You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, 
# and any egg dropped at or below floor F will not break.

# Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 

# Your goal is to know with certainty what the value of F is.

# What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?

 

# Example 1:

# Input: K = 1, N = 2
# Output: 2
# Explanation: 
# Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
# Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
# If it didn't break, then we know with certainty F = 2.
# Hence, we needed 2 moves in the worst case to know what F is with certainty.
# Example 2:

# Input: K = 2, N = 6
# Output: 3
# Example 3:

# Input: K = 3, N = 14
# Output: 4

# dp[n][k]: dp[n][K]means that, given k eggs and M moves, what is the maximum number of floor that we can check.
# The dp equation is:
# dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1,
# which means we take 1 move to a floor,
# if egg breaks, then we can check dp[m - 1][k - 1] floors.
# if egg doesn't breaks, then we can check dp[m - 1][k] floors.
# transition: 
# ����ÿ���ڵ�ǰû��check��¥����м�һ���ӣ�����3��������һ��1-8�㣬������4����(dp[3][8])��������ˣ���ôdp
# ��Ϊ���������һ���ڵ�ǰ��û��: we check dp[m - 1][k]��һ�����ڵ�ǰ������
# �ܵ�¥���� = ¥�ϵ�¥���� + ¥�µ�¥���� + 1
# 1�����������Ĳ�¥�Ӽ���������ֻ����ˤ�����ûˤ�飬���˵Ļ��Ͳ�¥�£�û��Ļ��Ͳ�¥�ϡ�
# 2����������¥������¥���ܵ�¥���� = ¥�ϵ�¥���� + ¥�µ�¥���� + 1����ǰ���¥����

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()
        # base cases
        if K == 1: return N
        if N == 0: return 0
        dp = [[0] * (K + 1) for i in range(N + 1)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            if dp[m][K] >= N: 
                return m