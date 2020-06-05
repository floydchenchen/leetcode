# 10. Regular Expression Matching

# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.



class Solution:
    # solution 1: recursive solution
    # break the problem into 3 sub-problems/cases to reduce the length of s and p

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return s == ""
        
        # case 1: if we encounter '*', (1) we reduce the length of p, or (2) reduce the length of s
        # (1) reduce p: e.g. p starts with "a*", so it counts as "", we only match s with p[2:]
        # (2) reduce s: s[0] matches p[0] OR p[0] is '.', then we match s[1:] with p
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or \
                   (len(s) > 0 and (s[0] == p[0] or p[0] == '.')) and (self.isMatch(s[1:], p))

        # case 2: if we encounter '.', then we reduce both s and p by matching s[1:] with p[1:]
        elif p[0] == '.':
            return len(s) > 0 and self.isMatch(s[1:], p[1:])

        # case 3: matching with normal char, we reduce both s and p by matching s[1:] with p[1:]
        return len(s) > 0 and s[0] == p[0] and self.isMatch(s[1:], p[1:])

    # dp solution
    # we can store s' and p's substring matching result
    # The DP table and the string s and p use the same indexes i and j, but
    # memo[i][j] means the match status between p[:i] and s[:j], i.e.
    # memo[0][0] means the match status of two empty strings, and
    # memo[1][1] means the match status of p[0] and s[0]. Therefore, when
    # refering to the i-th and the j-th characters of p and s for updating
    # memo[i][j], we use p[i - 1] and s[j - 1].

    # 1. If p[j] == s[i]:  dp[i][j] = dp[i-1][j-1];
    # 2. If p[j] == '.' : dp[i][j] = dp[i-1][j-1]; (实质和(1.)是一样的)
    # 3. If p[j] == '*':
    #    here are two sub conditions:
    #        1   if p[j-1] != s[i] : dp[i][j] = dp[i][j-2], in this case, a* only counts as empty
    #        2   if p[j-1] == s[i] or p[i-1] == '.':
    #             dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a
    #             or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
    #             or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty
    
    def isMatch_v2(self, s, p):
        if s is None or p is None:
            return False

        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        dp[0][0] = True
        print(dp)
        for i in range(len(p)):
            if p[i] == "*" and dp[0][i-1]:
                dp[0][i+1] = True

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == ".":
                    dp[i+1][j+1] = dp[i][j]
                if p[j] == s[i]:
                    dp[i+1][j+1] = dp[i][j]
                if p[j] == '*':
                    if p[j-1] != s[i] and p[j-1] != ".":
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else:
                        dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1] or dp[i+1][j-1]
        return dp[-1][-1]

    # cleaner recursive method
    def isMatch_v3(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        # case 1: if we encounter '*', (1) we reduce the length of p, or (2) reduce the length of s
        # (1) reduce p: e.g. p starts with "a*", so it counts as "", we only match s with p[2:]
        # (2) reduce s: s[0] matches p[0] OR p[0] is '.', then we match s[1:] with p
        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        # case 2: normal matching or we encounter '.'
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
    
    # top down memo recursive method
    def isMatch_v4(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                # exit
                if j == len(pattern):
                    result = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j + 1 < len(pattern) and pattern[j+1] == '*':
                        result = dp(i, j+2) or first_match and dp(i + 1, j)
                    else:
                        result = first_match and dp(i + 1, j + 1)

                memo[i, j] = result
            return memo[i, j]

        return dp(0, 0)

sol = Solution()
print(sol.isMatch_v2("aab", "c*a*b"))


