# 472. Concatenated Words

# Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

# Example:
# Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
#  "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

from typing import List
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        memo = set()
        def dfs(word: str) -> bool:
            if word in memo:
                return True
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in wordSet and suffix in wordSet:
                    memo.add(word)
                    print("memo", memo)
                    return True
                if prefix in wordSet and dfs(suffix):
                    return True
                if suffix in wordSet and dfs(prefix):
                    return True
            
            return False
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        
        return res

sol = Solution()
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(sol.findAllConcatenatedWordsInADict(words))