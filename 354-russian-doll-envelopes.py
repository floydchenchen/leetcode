# 354. Russian Doll Envelopes

# You have a number of envelopes with widths and heights given as a pair of integers (w, h).
# One envelope can fit into another if and only if both the width and height of one envelope is
# greater than the width and height of the other envelope.
#
# What is the maximum number of envelopes can you Russian doll? (put one inside other)
#
# Example:
# Given envelopes = [[5,4],[6,4],[6,7],[2,3]],
# the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).


# the problem can be reduced to finding the length of longest increasing subsequence
# The idea is to order the envelopes and then calculate the longest increasing subsequence (LISS).
# We first sort the envelopes by width, and we also make sure that when the width is the same,
# the envelope with greater height comes first. Why? This makes sure that when we calculate the LISS,
# we don't have a case such as [3, 4] [3, 5] (we could increase the LISS but this would be wrong as the width is
# the same. It can't happen when [3, 5] comes first in the ordering).
import bisect
class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        # lambda expression comparator!
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        dp = []
        # enumerate!
        # LC300. find the longest increasing subsequence (DP)
        # dp[i]: smallest tail element for a subsequence with length i
        for index, element in enumerate(envelopes):
            insert_index = bisect.bisect_left(dp, element[1])
            if insert_index < len(dp):
                dp[insert_index] = element[1]
            else:
                dp.append(element[1])
        print("dp", dp)
        return len(dp)

sol = Solution()
print(sol.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
