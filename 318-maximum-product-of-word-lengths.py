# 318. Maximum Product of Word Lengths

# Given a string array words, find the maximum value of length(word[i]) * length(word[j])
# where the two words do not share common letters.
# You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
#
# Example 1:
#
# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".
# Example 2:
#
# Input: ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".
# Example 3:
#
# Input: ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.

from collections import defaultdict
class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic = defaultdict(int)
        for word in words:
            mask = 0
            for c in set(word):
                mask |= (1 << (ord(c) - ord("a")))
            dic[mask] = max(dic[mask], len(word))
        return max([dic[x] * dic[y] for x in dic for y in dic if not x & y] or [0])

print(Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))