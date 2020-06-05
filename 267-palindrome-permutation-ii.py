# 267. Palindrome Permutation II

# Given a string s, return all the palindromic permutations (without duplicates) of it.
# Return an empty list if no palindromic permutation could be form.
#
# Example 1:
#
# Input: "aabb"
# Output: ["abba", "baab"]
# Example 2:
#
# Input: "abc"
# Output: []

from collections import Counter
class Solution:
    def generatePalindromes(self, s):

        def dfs(end, tmp, result):
            if len(tmp) == end:
                cur = ''.join(tmp)
                result.append(cur + mid + cur[::-1])
            else:
                for i in range(end):
                    if visited[i] or (i > 0 and half[i] == half[i - 1] and not visited[i - 1]):
                        continue
                    visited[i] = True
                    tmp.append(half[i])
                    dfs(end, tmp, result)
                    visited[i] = False
                    tmp.pop()

        counter = Counter(s)
        # put all odd occurrences chars in the middle
        mids = [k for k, v in counter.items() if v % 2 == 1]
        # like in 266. palindrome permutation, check if we cannot form any permutations
        if len(mids) > 1:
            return []
        mid = "" if not mids else mids[0]
        # 将counter中所有的key组成一个每个key都出现了一半次数的list
        # 例如{"a":4, "b": 2} ==> half = ["a", "a", "b"]
        half = list(''.join([k * (v // 2) for k, v in counter.items()]))

        result = []
        visited = [False] * len(half)
        dfs(len(half), [], result)
        return result

print(Solution().generatePalindromes("aaaabb"))