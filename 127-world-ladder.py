# 127. Word Ladder

# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest
# transformation sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

# BFS 找最短路径
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = [[beginWord, 1]]
        while queue:
            word, length = queue.pop(0)
            # 退出条件
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in wordList:
                        # 剪枝：从wordList中remove当前的word，减少运算量
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0


sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
