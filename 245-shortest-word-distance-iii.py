# 245. Shortest Word Distance III

# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
# word1 and word2 may be the same and they represent two individual words in the list.
#
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Input: word1 = “makes”, word2 = “coding”
# Output: 1
# Input: word1 = "makes", word2 = "makes"
# Output: 3
# Note:
# You may assume word1 and word2 are both in the list.

# 思路：思路基本和243相同，但是多加一个boolean "same" pointer
# 如果same，在match word1的时候，在update result了之后，也同时更新i2
class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1 = i2 = result = len(words)
        same = word1 == word2
        for i in range(len(words)):
            if words[i] == word1:
                i1 = i
                result = min(result, abs(i1 - i2))
                if same:
                    i2 = i1
            elif not same and words[i] == word2:
                i2 = i
                result = min(result, abs(i1 - i2))
        return result
