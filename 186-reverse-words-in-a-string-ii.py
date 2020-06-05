# 186. Reverse Words in a String II

# Given an input string , reverse the string word by word.
#
# Example:
#
# Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# Note:
#
# A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing spaces.
# The words are always separated by a single space.
# Follow up: Could you do it in-place without allocating extra space?

class Solution:
    # 三步翻转法
    def reverseWords(self, s):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        def reverse(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        # 1. reverse the whole sentence
        reverse(s, 0, len(s) - 1)

        # 2. reverse each word
        start = 0
        for i in range(len(s)):
            # 遇到" "，就翻转前面
            if s[i] == " ":
                reverse(s, start, i - 1)
                start = i + 1

        # reverse the last word, 同时处理edge case: if there is only one word，我们不会遇到" "
        reverse(s, start, len(s) - 1)
        # print(s)

Solution().reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])