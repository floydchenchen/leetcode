# 212. Word Search II

# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells
# are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
# Example:
#
# Input:
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
#
# Output: ["eat","oath"]
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.

# 思路：和word search I 的区别：word search I 只需要return True or False，word search II 需要输出所有的字典里能找到的词

from collections import defaultdict


class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.is_word = True

    # def search(self, word):
    #     curr = self.root
    #     for char in word:
    #         curr = curr.children.get(char)
    #         if not curr:
    #             return False
    #     return curr.is_word


class Solution:
    def findWords(self, board, words):

        def dfs(board, node, i, j, path, result):
            if node.is_word:
                result.append(path)
                node.is_word = False
            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                c = board[i][j]
                node = node.children.get(c)
                if not node:
                    return
                board[i][j] = "#"
                dfs(board, node, i + 1, j, path + c, result)
                dfs(board, node, i - 1, j, path + c, result)
                dfs(board, node, i, j + 1, path + c, result)
                dfs(board, node, i, j - 1, path + c, result)
                board[i][j] = c

        result = []
        trie = Trie()
        node = trie.root
        for word in words:
            trie.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, node, i, j, "", result)
        return result
