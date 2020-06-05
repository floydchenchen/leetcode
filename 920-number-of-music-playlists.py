# 920. Number of Music Playlists

# Your music player contains N different songs and she wants to listen to L (not necessarily different) songs
# during your trip.  You create a playlist so that:
#
# Every song is played at least once
# A song can only be played again only if K other songs have been played
# Return the number of possible playlists.  As the answer can be very large, return it modulo 10^9 + 7.
#
#
#
# Example 1:
#
# Input: N = 3, L = 3, K = 1
# Output: 6
# Explanation: There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].
# Example 2:
#
# Input: N = 2, L = 3, K = 0
# Output: 6
# Explanation: There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]
# Example 3:
#
# Input: N = 2, L = 3, K = 1
# Output: 2
# Explanation: There are 2 possible playlists. [1, 2, 1], [2, 1, 2]

# "A song can only be played again only if K other songs have been played."
# I think this sentence is a little bit ambiguous.
# Actually, in this problem it means there must be at least K other songs between two same songs,
# instead of K other songs since the beginning.

# dp[N][L]: the max different combination we have when we use N different songs at position L
# transition: dp[N][L] = dp[N-1][L-1] * N +
# if use a new music dp[N-1][L-1] * N, simple combination
# if not use a new music: dp[N][L-1] * (N - K), N - K means the new song should be different from the last K songs

import math
class Solution:
    # dp[N][L]:
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        dp = [[0] * (L + 1) for _ in range(N + 1) ]
        for i in range(K + 1, N + 1):
            for j in range(i, L + 1):
                if i == j or i == K + 1:
                    dp[i][j] = math.factorial(i)
                else:
                    dp[i][j] = dp[i - 1][j - 1] * i + dp[i][j - 1] * (i - K)
        return dp[N][L] % (10**9 + 7)
