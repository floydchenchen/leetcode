# 395. Longest Substring with At Least K Repeating Characters

# Find the length of the longest substring T of a given string (consists of lowercase letters only)
# such that every character in T appears no less than k times.
#
# Example 1:
#
# Input:
# s = "aaabb", k = 3
#
# Output:
# 3
#
# The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:
#
# Input:
# s = "ababbc", k = 2
#
# Output:
# 5
#
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

from collections import Counter
class Solution:
    # solution 1: divide and conquer
    # 先将所有的c放到set中，再扫一遍set，看c出现的次数是否 < k，如果是那么用c作为separator将s分为若干个substring
    # 再recursively搜每个substring
    def longestSubstring(self, s, k):
        for c in set(s):
            # 或者可用counter
            if s.count(c) < k:
                return max(self.longestSubstring(sub_s, k) for sub_s in s.split(c))
        return len(s)

    # def longestSubstring1(self, s, k):
    #     result = 0
    #     if len(s) < k:
    #         return result
    #     dic = Counter(s)
    #     # set 里存出现次数不到k次的char
    #     _set = set()
    #     for k, v in dic.items():
    #         if v <= k:
    #             _set.add(v)
    #
    #     # edge case, every c in s repeats at least k times
    #     if not _set:
    #         return len(s)
    #
    #     l = 0
    #     while l < len(s):
    #         r = l
    #         #
    #         while r < len(s) and s[r] not in _set:
    #             r += 1
    #         if r > l:
    #             result = max(result, r - l + 1)






