# 856. Score of Parentheses

# Given a balanced parentheses string S, compute the score of the string based on the following rule:

# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
 

# Example 1:

# Input: "()"
# Output: 1
# Example 2:

# Input: "(())"
# Output: 2
# Example 3:

# Input: "()()"
# Output: 2
# Example 4:

# Input: "(()(()))"
# Output: 6

# cur record the score at the current layer level.

# If we meet '(',
# we push the current score to stack,
# enter the next inner layer level,
# and reset cur = 0.

# If we meet ')',
# the cur score will be doubled and will be at least 1.
# We exit the current layer level,
# and set cur = stack.pop() + cur

# Complexity: O(N) time and O(N) space

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0] # The score of the current frame
        for i in S:
            if i == '(':
                stack.append(0)
            else:
                cur_score = stack.pop()
                stack[-1] += max(2 * cur_score, 1)
        return stack.pop()
                