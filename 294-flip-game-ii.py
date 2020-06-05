# 294. Flip Game II

# You are playing the following Flip Game with your friend: Given a string that contains only these two characters:
# + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can
# no longer make a move and therefore the other person will be the winner.
#
# Write a function to determine if the starting player can guarantee a win.
#
# Example:
#
# Input: s = "++++"
# Output: true
# Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
# Follow up:
# Derive your algorithm's runtime complexity.

class Solution:
    # Without memoization:
    # ~ 3150 ms
    def canWin(self, s):
        return any(s[i:i + 2] == '++' and not self.canWin(s[:i] + '-' + s[i + 2:])
                   for i in range(len(s)))

    # With memoization:
    # ~ 130 ms
    _memo = {}
    def canWin1(self, s):
        memo = self._memo
        if s not in memo:
            memo[s] = any(s[i:i + 2] == '++' and not self.canWin1(s[:i] + '-' + s[i + 2:])
                          for i in range(len(s)))
        return memo[s]
