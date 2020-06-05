# 72. Edit Distance
#
# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character

# 思路：dp[i][j]: 把word1[0:i]变到wor2[0:j]的最小操作
# transition: 如果word1[i-1] == word2[j-1]，则dp[i][j] = dp[i-1][j-1]，否则需要对word1进行replace / delete / insert
# dp[i][j] = min(replace, delete_word1, delete_word2)
# replace = dp[i-1][j-1] + 1
# delete_word1 = dp[i-1][j] + 1
# delete_word2 = dp[i][j-1] + 1
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1, len2 = len(word1), len(word2)
        # dp[i][j]: the minimum number of operations to convert word1[0:i] to word2[0:j]
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        # initialize, 相当于每次都删一个，删到0
        for i in range(len1 + 1):
            dp[i][0] = i
        for j in range(len2 + 1):
            dp[0][j] = j

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # matching
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # plus 1 step to match
                    replace = dp[i-1][j-1] + 1
                    # delete减少一个word1的字母，所以i-1
                    delete_word1 = dp[i-1][j] + 1
                    # insert相当于减少一个word2的字母，所以j-1
                    delete_word2 = dp[i][j-1] + 1
                    dp[i][j] = min(replace, delete_word1, delete_word2)
        return dp[len1][len2]
