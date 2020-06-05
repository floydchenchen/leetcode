# 269. Alien Dictionary

# There is a new alien language whichar uses the latin alphabet. However, the order among letters are unknown to you.
# You receive a list of non-empty words from the dictionary, where words are sorted lexicographically
# by the rules of this new language. Derive the order of letters in this language.
#
# Example 1:
#
# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
#
# Output: "wertf"
# Example 2:
#
# Input:
# [
#   "z",
#   "x"
# ]
#
# Output: "zx"
# Example 3:
#
# Input:
# [
#   "z",
#   "x",
#   "z"
# ]
#
# Output: ""
#
# Explanation: The order is invalid, so return "".


# 思路：topological sort
# topological sort模板
# 1. build the graph with incoming degrees represented by am 1d array
# 2. identify vertices that have no incoming edge (there's a cycle if no suchar vertex exists), put it in queue
# 3. repeat step 2
# from collections import defaultdict
# class Solution(object):
#     # topological sorting
#     def alienOrder(self, words):
#         """
#         :type words: List[str]
#         :rtype: str
#         """
#         # build map, map<c, set>: the set of chars that occurs after c
#         # degree存的是这个char c有多少个prerequisite
#         map, degree = defaultdict(set), {}
#         result = []
#         if not words:
#             return ""

#         # 1.0 initialize degree map
#         for word in words:
#             for c in word:
#                 if c not in degree:
#                     degree[c] = 0

#         # 1.1 compare two words
#         for i in range(len(words) - 1):
#             x, y = words[i], words[i+1]
#             # compare two characters
#             min_len = min(len(x), len(y))
#             for j in range(min_len):
#                 # 如果x[j] != y[j]，那么x[j]出现在y[j]之前
#                 if x[j] != y[j]:
#                     if y[j] not in map[x[j]]:
#                         map[x[j]].add(y[j])
#                         degree[y[j]] += 1
#                     break

#         # 2. first build and initialize the queue
#         q = []
#         for k in degree.keys():
#             if degree[k] == 0:
#                 q.append(k)

#         # 3. topological sort
#         while q:
#             k = q.pop(0)
#             result.append(k)
#             if k in map:
#                 for c in map[k]:
#                     degree[c] -= 1
#                     if degree[c] == 0:
#                         q.append(c)

#         return "".join(result) if len(degree) == len(result) else ""



from collections import defaultdict
from typing import List
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 分别储存这个node的parents和children
        children, parents = {}, {}
        for word in words:
            for char in word:
                children[char] = set()
                parents[char] = set()

        for word1, word2 in zip(words[:-1], words[1:]):
            # judge if word1 and word2 are valid
            # for example word1='abc' and word2='ab' then we cannot get a valid result
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return ""

            # extract the relation
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    # char1 is the parent of char2, and char2 is the child of char1
                    children[char1].add(char2)
                    parents[char2].add(char1)
                    break
        print("children", children)
        print("parents", parents)

        # topological sort
        result, q = [], []
        # 因为我们要随时删除parents[node]，这样才会不影响for loop
        no_parents_list = [char for char in parents if len(parents[char]) == 0]
        print("no_parents_list", no_parents_list)
        for char in no_parents_list:
            del parents[char]
            q.append(char)
        print("q", q)

        while q:
            char = q.pop(0)
            result.append(char)
            # remove the current char as the parent of its children
            for child in children[char]:
                parents[child].remove(char)
                # 判断这个node是否变成了no-parent node
                if len(parents[child]) == 0:
                    q.append(child)
                    del parents[child]
        # 如果parents还是不为空的话，说明没有valid answer
        if parents:
            return ""
        return "".join(result)
sol = Solution()
print(sol.alienOrder(["wrt","wrf","er","ett","rftt"]))
# print(sol.alienOrder(["za","zb","ca","cb"]))
