# 5. Longest Palindromic Substring

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"

# idea: memo[i][j] represents whether s(i:j) can form a palindromic substring,
# memo[i][j] is true when s[i] == s[j] and s(i+1:j-1) is a palindromic substring
# transition function: memo[i][j] = s[i] == s[j] and (j - i < 3 or memo[i+1][j-1])

class Solution:
    # bottom-up dp solution: O(n^2) time, O(n^2) space
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # initialize a 2d array
        # https://stackoverflow.com/questions/24023115/how-to-initialise-a-2d-array-in-python
        result = ""
        n = len(s)
        memo = [[0 for _ in range(n)] for _ in range(n)]
        # dp[i][j]: s(i:j)是否能形成一个palindrome
        # i starts from the end; j starts from the beginning
        # 注意transition fucntion是dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i+1][j-1])
        # 所以i得从右往左，而j从左往右（transition的方向）
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                memo[i][j] = s[i] == s[j] and (j - i < 3 or memo[i+1][j-1])
                # 更新result
                if memo[i][j] and (result == "" or j - i + 1 > len(result)):
                    result = s[i:j+1]
        return result

    # bottom-up dp solution improvement: O(n^2) time, O(n) space
    def longestPalindrome_v2(self, s):
        """
        :type s: str
        :rtype: str
        """
        # initialize a 2d array
        # https://stackoverflow.com/questions/24023115/how-to-initialise-a-2d-array-in-python
        result = ""
        n = len(s)
        memo = [0] * n
        # i starts from the end; j starts from the beginning
        for i in range(n - 1, -1, -1):
            # j changes to decrement compared to the original solution
            for j in range(n - 1, i - 1, -1):
                memo[j] = s[i] == s[j] and (j - i < 3 or memo[j-1])
                if memo[j] and (result == "" or j - i + 1 > len(result)):
                    result = s[i:j+1]
        return result

    # ----------------------------------------------------------------------------
    # https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints
    # extend_palindrome solution
    start, end = 0, 0
    def longestPalindrome_solution_2(self, s):
        n = len(s)
        if n < 2:
            return s

        for i in range(n - 1):
            # palindrome might have even or odd length
            self.extend_palindrome(s, i, i)
            self.extend_palindrome(s, i, i + 1)
        return s[self.start: self.end + 1]

    def extend_palindrome(self, s, i, j):
        # 这里不能把 i >= 0, j <= len(s) 换成 i - 1 >= 0 and j + 1 < len(s)... 同时去掉while-loop后面的 i += 1, j -= 1
        # 因为这样的话我们就并没有在比较s[i] == s[j]了，而是直接从s[i-1] == s[j+1]开始比较了
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1

        # don't forget to get the two pointers back
        i += 1
        j -= 1

        # if the substring ls longer, update start and end
        if j - i > self.end - self.start:
            self.start = i
            self.end = j
