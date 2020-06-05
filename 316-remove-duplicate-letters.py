# 316. Remove Duplicate Letters

# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and
# only once. You must make sure your result is the smallest in lexicographical order among all possible results.
#
# Example 1:
#
# Input: "bcabc"
# Output: "abc"
# Example 2:
#
# Input: "cbacdcbc"
# Output: "acdb"

# 思路：
# 1. 先找到每个c出现的最后index，放进last_index_dic
# 2. for loop扫过s，如果result中没有s[i]，while(如果s[i]小于result[-1]，而且i在result[-1]的last index之前，直接去掉result[-1])
# 把s[i]插入到合适的result位置
class Solution:
    def removeDuplicateLetters(self, s):
        # last index dict
        last_index_dic = {c: i for i, c in enumerate(s)}
        result = []
        for i in range(len(s)):
            if s[i] not in result:
                while result and s[i] < result[-1] and i < last_index_dic[result[-1]]:
                    del result[-1]
                result.append(s[i])
        return "".join(result)

print(Solution().removeDuplicateLetters("cbacdcbc"))