# 394. Decode String

# Given an encoded string, return it's decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being
# repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only
# for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
#
# Examples:
#
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

# 用stack存[char, char_freq]
class Solution:
    def decodeString(self, s):
        # stack中存的是[char, char_freq]
        stack = []
        stack.append(["", 1])
        num = ""
        for c in s:
            if c.isdigit():
                num += c
            elif c == '[':
                stack.append(["", int(num)])
                num = ""
            elif c == ']':
                char, char_freq = stack.pop()
                stack[-1][0] += char * char_freq
            else:
                stack[-1][0] += c
        return stack[0][0]

print(Solution().decodeString("3[a2[c]]"))