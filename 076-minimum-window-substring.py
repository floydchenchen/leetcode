# 76. Minimum Window Substring

# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
#
# Example:
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"

from collections import defaultdict
import math
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # put all characters in a map
        dic = defaultdict(int)
        for c in t:
            dic[c] += 1

        l, r, counter = 0, 0, len(dic)
        min_len, min_start = math.inf, 0
        while r < len(s):
            # 将右边包括在window中
            if s[r] in dic:
                dic[s[r]] -= 1
                if dic[s[r]] == 0:
                    counter -= 1
            r += 1

            # if counter == 0: we have a valid window now, fid the minimum window by moving i
            while counter == 0:
                if min_len > r - l:
                    min_len = r - l
                    min_start = l

                # when move l to the right and we need that char in the window
                # we lose the needed char in the window, so we update the dic
                # 将s[l]移出window
                if s[l] in dic:
                    dic[s[l]] += 1
                    if dic[s[l]] > 0:
                        counter += 1
                l += 1

        return "" if min_len == math.inf else s[min_start: min_start + min_len]


