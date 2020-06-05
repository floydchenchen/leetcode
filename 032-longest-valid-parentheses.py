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

    # stack中存的数字：每个"("组成多少个"()"，
    # 例如"()(()"，stack的变化：
    # [0]
    # [0, 0]
    # [2]
    # [2, 0]
    # [4]
    # [0]   
    # 所以最大是2
    def longestValidParentheses(self, s):
        stack = [0]
        result = 0
        for c in s:
            # stack中存的是，当前valid的这个substring，有多少个valid括号组合
            if c == "(":
                stack.append(0)
            else:
                # skip the leading ")"
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    result = max(result, stack[-1])
                else:
                    # 清零
                    stack = [0]
            print(stack)
        return result

# print(Solution().longestValidParentheses("()(()"))
print(Solution().longestValidParentheses(")()())"))