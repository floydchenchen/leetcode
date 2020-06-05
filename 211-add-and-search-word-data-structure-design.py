# 211. Add and Search Word - Data structure design

# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A .
# means it can represent any one letter.
#
# Example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word):
        curr = self.root
        result = [False]
        self.dfs(curr, word, result)
        return result[0]

    # use result as a global variable
    # recursive dfs solution
    def dfs(self, curr, word, result):
        # exit
        if not word:
            if curr.is_word:
                result[0] = True
            return
        # dfs for every child if regex
        if word[0] == ".":
            for child in curr.children.values():
                self.dfs(child, word[1:], result)
        # normal search
        else:
            curr = curr.children.get(word[0])
            if not curr:
                return
            self.dfs(curr, word[1:], result)
