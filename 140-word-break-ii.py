# 140. Word Break II

# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# add spaces in s to construct a sentence where each word is a valid dictionary word.
# Return all such possible sentences.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# Example 2:
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []


# memo(i) returns a list of all sentences that can be built from the suffix s[i:].
# top down memo dfs (top down dp)
class Solution:
    def wordBreak(self, s, wordDict):
        memo = {}
        
        def dfs(s):
            result = []
            if s in memo:
                return memo[s]
            if not s:
                return result

            for word in wordDict:
                if not s.startswith(word):
                    continue
                # exit
                if len(word) == len(s):
                    result.append(word)
                else:
                    rest_result = dfs(s[len(word):])
                    for item in rest_result:
                        item = word + " " + item
                        result.append(item)
            memo[s] = result
            return result

        return dfs(s)