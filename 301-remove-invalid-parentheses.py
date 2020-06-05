# 301. Remove Invalid Parentheses

# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
#
# Note: The input string may contain letters other than the parentheses ( and ).
#
# Example 1:
#
# Input: "()())()"
# Output: ["()()()", "(())()"]

# Example 2:
#
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]

# Example 3:
#
# Input: ")("
# Output: [""]

class Solution:
    # BFS Solution
    def removeInvalidParentheses(self, s):
        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0
        level = {s}
        while True:
            # filter掉not valid的string
            valid = list(filter(isvalid, level))
            print(valid)
            # 因为要minimum moves，所以只需要有valid，马上print所有的valid substrings
            if valid:
                return valid
            # 每次去掉一个字符，放进set（去重复）
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}
            print(level)

    # DFS solution
    def removeInvalidParentheses1(self, s):
        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0

        def dfs(s, start, left, right, result):
            if isvalid(s):
                result.append(s)
            for i in range(start, len(s)):
                # 如果"("多了
                if s[i] == "(" and left:
                    #  s[i] != s[i-1]: 避免重复！因为两个重复的"(("，移除哪一个都是一样的
                    if i == start or s[i] != s[i-1]:
                        # 去除这一个"("
                        dfs(s[:i] + s[i+1:], i, left - 1, right, result)
                # 如果")"多了
                if s[i] == ')' and right:
                    if i == start or s[i] != s[i - 1]:
                        dfs(s[:i] + s[i+1:], i, left, right - 1, result)

        # 用left和right分别记录多余的左括号和右括号的数量
        left, right = 0, 0
        for c in s:
            if c == "(":
                left += 1
            else:
                if not left:
                    right += c == ')'
                else:
                    left -= c == ')'
        result = []
        dfs(s, 0, left, right, result)
        return result

sol = Solution()
print(sol.removeInvalidParentheses("(a)))"))