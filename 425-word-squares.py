# 425. Word Squares

# Given a set of words (without duplicates), find all word squares you can build from them.
#
# A sequence of words forms a valid word square if the kth row and column read the exact same string,
# where 0 ≤ k < max(numRows, numColumns).
#
# For example, the word sequence ["ball","area","lead","lady"]
# forms a word square because each word reads the same both horizontally and vertically.
#
# b a l l
# a r e a
# l e a d
# l a d y
# Note:
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.
# Example 1:
#
# Input:
# ["area","lead","wall","lady","ball"]
#
# Output:
# [
#   [ "wall",
#     "area",
#     "lead",
#     "lady"
#   ],
#   [ "ball",
#     "area",
#     "lead",
#     "lady"
#   ]
# ]
#
# Explanation:
# The output consists of two word squares. The order of output does not matter
# (just the order of words in each word square matters).
# Example 2:
#
# Input:
# ["abat","baba","atan","atal"]
#
# Output:
# [
#   [ "baba",
#     "abat",
#     "baba",
#     "atan"
#   ],
#   [ "baba",
#     "abat",
#     "baba",
#     "atal"
#   ]
# ]
#
# Explanation:
# The output consists of two word squares. The order of output does not matter
# (just the order of words in each word square matters).

# 思路参考：https://leetcode.com/problems/word-squares/discuss/91333/Explained.-My-Java-solution-using-Trie-126ms-1616
# In order for this to work, we need to fast retrieve all the words with a given prefix.
from collections import defaultdict


# solution without trie

# 思路：
# wall      Try words      wall                     wall                      wall
# a...   => starting  =>   area      Try words      area                      area
# l...      with "a"       le..   => starting  =>   lead      Try words       lead
# l...                     la..      with "le"      lad.   => starting   =>   lady
#                                                             with "lad"

class Solution:
    def wordSquares(self, words):
        word_len = len(words[0])

        # build the prefix dictionary whose key is prefix and value is full word
        prefix_dic = defaultdict(list)
        for word in words:
            for i in range(word_len):
                prefix_dic[word[:i]].append(word)
        # print(prefix_dic)

        # recursive dfs
        def build(square, result):
            if len(square) == word_len:
                result.append(square)
                return
            for word in prefix_dic[''.join(list(zip(*square))[len(square)])]:
                # print(square)
                # print(''.join(list(zip(*square))[len(square)]))
                build(square + [word], result)

        result = []
        for word in words:
            build([word], result)
        return result


# solution with trie
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.prefix = set()
        self.is_word = False


class Solution1:
    def insert(self, root, words):
        for word in words:
            curr = root
            curr.prefix.insert(word)
            for char in word:
                curr = curr.children[char]
                curr.prefix.insert(word)
            curr.is_word = True

    def get_prefix_list(self, root, prefix):
        curr = root
        for char in prefix:
            curr = curr.children.get(char)
            if not curr:
                return []
        return list(curr.prefix)


sol = Solution()
sol.wordSquares(["ball","area","lead","lady"])