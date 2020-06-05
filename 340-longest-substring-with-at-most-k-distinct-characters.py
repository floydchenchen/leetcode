# 340. Longest Substring with At Most K Distinct Characters

# Given a string, find the length of the longest substring T that contains at most k distinct characters.
#
# Example 1:
#
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# Example 2:
#
# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.

# 思路：Use dictionary d to keep track of (character, location) pair
# 从左到右扫一遍，把右边新的s[right]存到dic中去，如果len(dic) > k了，找到left = dic中最左边的index，移除 and left += 1，
# 在每次for-loop结束之前更新substring长度的最大值
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dic = {}
        left, result = 0, 0
        for right, c in enumerate(s):
            dic[c] = right
            if len(dic) > k:
                left = min(dic.values())
                del dic[s[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
