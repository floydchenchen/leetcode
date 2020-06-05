# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    # solution 1: sort，比较第一个和最后一个即可
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        result = []
        a, b = strs[0], strs[-1]
        for i in range(len(a)):
            # 注意保证len(b) > i
            if len(b) > i and b[i] == a[i]:
                result.append(a[i])
            else:
                break
        return "".join(result)

    # solution 2: 两个while-loop找
    def longestCommonPrefix1(self, strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, c in enumerate(shortest):
            for s in strs:
                if s[i] != c:
                    return shortest[:i]
        return shortest

