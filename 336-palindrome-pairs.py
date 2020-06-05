# 336. Palindrome Pairs

# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list,
# so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
#
# Example 1:
#
# Input: ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

# 思路：把word倒过来作为key，存它在words中的index，作为一个dictionary
class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # 把word倒过来作为key，存它在words中的index
        # 把每个word都partition开，分为prefix和postfix，再来比较
        # ["abcd","dcba","lls","s","sssll"]
        # {'dcba': 0, 'abcd': 1, 'sll': 2, 's': 3, 'llsss': 4}
        dic = dict([(word[::-1], i) for i, word in enumerate(words)])
        result = []

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix, postfix = word[:j], word[j:]
                if prefix in dic and i != dic[prefix] and postfix == postfix[::-1]:
                    result.append([i, dic[prefix]])
                if j > 0 and postfix in dic and i != dic[postfix] and prefix == prefix[::-1]:
                    result.append([dic[postfix], i])

        return result


sol = Solution()
print(sol.palindromePairs(["abcd","dcba","lls","s","sssll"]))