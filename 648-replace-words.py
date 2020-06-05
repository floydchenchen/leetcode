# 648. Replace Words

# In English, we have a concept called root, which can be followed
# by some other words to form another longer word - let's call this word successor.
# For example, the root an, followed by other, which can form another word another.
#
# Now, given a dictionary consisting of many roots and a sentence.
# You need to replace all the successor in the sentence with the root forming it.
# If a successor has many roots can form it, replace it with the root with the shortest length.
#
# You need to output the sentence after the replacement.
#
# Example 1:
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word):
        curr = self.root
        for i, char in enumerate(word):
            if char not in curr.children:
                break
            curr = curr.children[char]
            if curr.is_word:
                return word[:i + 1]
        return word

    def replaceWords(self, dic, sentence):
        for word in dic:
            self.insert(word)
        sentence = sentence.split(" ")
        result = []
        for word in sentence:
            result.append(self.search(word))
        return " ".join(result)
