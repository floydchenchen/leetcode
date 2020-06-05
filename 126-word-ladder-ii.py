# 126. Word Ladder II

# Given two words (beginWord and endWordWord), and a dictionary's word list, find all shortest transformation
# sequence(s) from beginWord to endWordWord, such that:
#
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:
#
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWordWord are non-empty and are not the same.
# Example 1:
#
# Input:
# beginWord = "hit",
# endWordWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
# Example 2:
#
# Input:
# beginWord = "hit"
# endWordWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: []
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

# 思路：用dictionary: {word, set(parents)}来表示整个path，最后通过parents来build the result list
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        word_set = set(wordList)
        level = set([beginWord]) # 这个level有哪些node
        parents = defaultdict(set)
        while level and endWord not in parents:
            next_level = defaultdict(set)
            for word in level:
                for i in range(len(beginWord)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        n = word[:i] + char + word[i + 1:]
                        if n in word_set and n not in parents:
                            next_level[n].add(word)
                            # print("next_level", next_level)
            level = next_level
            # print("updated level", level)
            # The update() adds elements from a set (passed as an argument) to the set (calling the update() method)
            parents.update(next_level)
            # print("updated parents", parents)
            # print()
        result = [[endWord]]

        # BFS build the list
        while result and result[0][0] != beginWord:
            result = [[word] + path for path in result for word in parents[path[0]]]
            print(result)
        return result

print(Solution().findLadders("hit","cog",["hot","dot","dog","lot","log","cog"]))