# 642. Design Search Autocomplete System

# Design a search autocomplete system for a search engine.
# Users may input a sentence (at least one word and end with a special character '#').
# For each character they type except '#', you need to return the top 3 historical
# hot sentences that have prefix the same as the part of sentence already typed.
# Here are the specific rules:
#
# The hot degree for a sentence is defined as the number of times a user
# typed the exactly same sentence before.
# The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one).
# If several sentences have the same degree of hot, you need to use ASCII-code order
# (smaller one appears first).
# If less than 3 hot sentences exist, then just return as many as you can.
# When the input is a special character, it means the sentence ends, and in this case,
# you need to return an empty list.
# Your job is to implement the following functions:
#
# The constructor function:
#
# AutocompleteSystem(String[] sentences, int[] times): This is the constructor.
# The input is historical data. Sentences is a string array consists of previously typed sentences.
# Times is the corresponding times a sentence has been typed. Your system should record these historical data.
#
# Now, the user wants to input a new sentence. The following function will provide the next character the user types:
#
# List<String> input(char c): The input c is the next character typed by the user.
# The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#').
#  Also, the previously typed sentence should be recorded in your system.
# The output will be the top 3 historical hot sentences that have prefix
# the same as the part of sentence already typed.
#
#
# Example:
# Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
# The system have already tracked down the following sentences and their corresponding times:
# "i love you" : 5 times
# "island" : 3 times
# "ironman" : 2 times
# "i love leetcode" : 2 times
# Now, the user begins another search:
#
# Operation: input('i')
# Output: ["i love you", "island","i love leetcode"]
# Explanation:
# There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree.
# Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman".
# Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
#
# Operation: input(' ')
# Output: ["i love you","i love leetcode"]
# Explanation:
# There are only two sentences that have prefix "i ".
#
# Operation: input('a')
# Output: []
# Explanation:
# There are no sentences that have prefix "i a".
#
# Operation: input('#')
# Output: []
# Explanation:
# The user finished the input, the sentence "i a" should be saved as a historical sentence in system.
# And the following input will be counted as a new search.
#
# Note:
# The input sentence will always start with a letter and end with '#',
# and only one blank space will exist between two words.
# The number of complete sentences that to be searched won't exceed 100.
# The length of each sentence including those in the historical data won't exceed 100.
# Please use double-quote instead of single-quote when you write test cases even for a character input.
# Please remember to RESET your class variables declared in class AutocompleteSystem,
# as static/class variables are persisted across multiple test cases. Please see here for more details.


from collections import defaultdict
from heapq import *


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.hotness_dic = defaultdict(int)


class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.sentence = "" # 用self.sentence来代表当前input sentence的state
        self.curr = self.root # 用self.curr来代表当前cur node
        for i in range(len(sentences)):
            self.insert(sentences[i], times[i])

    def insert(self, word, count):
        curr = self.root
        for char in word:
            curr = curr.children[char]
            curr.hotness_dic[word] += count

    def input(self, c):
        # check if current char is "#"
        # if yes insert the sentence to the system and reset self.sentence and self.curr
        if c == "#":
            self.insert(self.sentence, 1)
            self.sentence = ""
            self.curr = self.root
            return []

        self.sentence += c
        self.curr = self.curr.children[c]
        heap, result = [], []
        # use heap to do sorting for output
        for sentence, count in self.curr.hotness_dic.items():
            heappush(heap, (-count, sentence))
        for i in range(3):
            if heap:
                _, sentence = heappop(heap)
                result.append(sentence)
        return result


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
acs = AutocompleteSystem(["i love you","island","iroman","i love leetcode"],[5,3,2,2])
print(acs.input("i"))
