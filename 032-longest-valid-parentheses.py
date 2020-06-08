# 32. Longest Valid Parentheses
# Given a string containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        # stack中记录valid parentheses的左边界
        # 为了应对")(())"即一开始就出现右括号的情况，对stack进行预处理
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len            

# print(Solution().longestValidParentheses("()(()"))
print(Solution().longestValidParentheses(")()())"))