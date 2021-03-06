# 917. Reverse Only Letters

# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place,
# and all letters reverse their positions.
#
#
#
# Example 1:
#
# Input: "ab-cd"
# Output: "dc-ba"
# Example 2:
#
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:
#
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"

class Solution:
    def reverseOnlyLetters(self, s):
        """
        :type S: str
        :rtype: str
        """
        chars = list(s)
        l, r = 0, len(chars) - 1
        while l < r:
            while l < r and not chars[l].isalpha():
                l += 1
            while l < r and not chars[r].isalpha():
                r -= 1
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1
        return "".join(chars)

sol = Solution()
# print(sol.reverseOnlyLetters("ab-cd"))
# print(sol.reverseOnlyLetters("a-bC-dEf-ghIj"))
# print(sol.reverseOnlyLetters("Test1ng-Leet=code-Q!"))
print(sol.reverseOnlyLetters("7_28]"))