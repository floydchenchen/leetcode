# 677. Map Sum Pairs

# Implement a MapSum class with insert, and sum methods.
#
# For the method insert, you'll be given a pair of (string, integer).
# The string represents the key and the integer represents the value.
# If the key already existed, then the original key-value pair will be overridden to the new one.
#
# For the method sum, you'll be given a string representing the prefix,
# and you need to return the sum of all the pairs' value whose key starts with the prefix.
#
# Example 1:
# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5

# trie
from collections import defaultdict


class TrieNode:
    def __init__(self):
        # each node keeps track of the total count of its children
        self.value = 0
        self.children = defaultdict(TrieNode)


class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, val):
        curr = self.root
        for char in key:
            curr = curr.children[char]
        curr.value = val

    # iterative bfs
    def sum(self, prefix):
        result = 0
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        stack = []
        stack.append(curr)
        while stack:
            node = stack.pop()
            result += node.value
            stack += node.children.values()
        return result

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
