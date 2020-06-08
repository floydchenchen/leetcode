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

# 思路：用dictionary: {word, set(parents)}来表示整个path，最后通过parents来build the result list，因为生成的图形毕竟不是一个tree，而是一个graph
# 用level来存当前level有哪些word，来避免重复（例如example 1中level 3有dog和log，如果不记录level的话，log也可以是dog的下一个word，而这样不对。）
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        word_set = set(wordList)
        level = defaultdict(set) # 这个level有哪些node
        level[beginWord] = set()
        parents = defaultdict(set)
        # build graph
        while level and endWord not in parents:
            next_level = defaultdict(set)
            for word in level:
                for i in range(len(beginWord)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        n = word[:i] + char + word[i + 1:]
                        if n in word_set and n not in parents:
                            next_level[n].add(word)
                            print("next_level", next_level)
            level = next_level
            # print("updated level", level)
            # The update() adds elements from a set (passed as an argument) to the set (calling the update() method)
            parents.update(next_level)
        print("parents", parents)
        
        q = []
        if endWord not in parents:
            return q
        # # BFS build the list
        # q.append([endWord])
        # cur_level = 1
        # while q and q[0][0] != beginWord:
        #     while len(q[0]) == cur_level:
        #         words = q.pop(0)
        #         for par in parents[words[0]]:
        #             q.append([par] + words)
        #     cur_level += 1
        # return q

        # backtrack build result
        def backtrack(result, temp, word):
            # exit
            if word == beginWord:
                result.append(list(temp))
            else:
                for parent in parents[word]:
                    temp.insert(0, parent)
                    backtrack(result, temp, parent)
                    temp.pop(0)
        
        result = []
        backtrack(result, [endWord], endWord)
        return result
            

print(Solution().findLadders("hit","cog",["hot","dot","dog","lot","log","cog"]))