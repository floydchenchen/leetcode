# 243. Shortest Word Distance

# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# Input: word1 = "makes", word2 = "coding"
# Output: 1

# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

# 思路：两个word，两个pointers。扫一遍array，找到match的word，就更新相应pointer，同时更新result的最小值
class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1 = i2 = result = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                i1 = i
                result = min(result, abs(i1 - i2))
            if words[i] == word2:
                i2 = i
                result = min(result, abs(i1 - i2))
        return result
