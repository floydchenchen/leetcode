# 358. Rearrange String k Distance Apart

# Given a non-empty string s and an integer k, rearrange the string such that the same characters are
# at least distance k from each other.
#
# All input strings are given in lowercase letters. If it is not possible to rearrange the string,
# return an empty string "".
#
# Example 1:
#
# Input: s = "aabbcc", k = 3
# Output: "abcabc"
# Explanation: The same letters are at least distance 3 from each other.
# Example 2:
#
# Input: s = "aaabc", k = 3
# Output: ""
# Explanation: It is not possible to rearrange the string.
# Example 3:
#
# Input: s = "aaadbbcc", k = 2
# Output: "abacabcd"
# Explanation: The same letters are at least distance 2 from each other.

from collections import Counter
from heapq import *
class Solution:
    def rearrangeString(self, str, k):
        heap = [(-freq, char)
                for char, freq in Counter(str).items()]
        heapify(heap)
        res = []
        while len(res) < len(str):
            if not heap: return ""
            freq, char = heappop(heap)
            temp_list = []
            res.append(char)
            for j in range(k - 1):
                # exit
                if len(res) == len(str):
                    return "".join(res)
                # if not possible to rearrange the string
                if not heap:
                    return ""
                fre, next = heappop(heap)
                res.append(next)
                if fre < -1:
                    temp_list.append((fre+1, next))
            for item in temp_list:
                heappush(heap, item)
            heappush(heap, (freq+1, char))
        return "".join(res)

print(Solution().rearrangeString("aabbcc", 3))