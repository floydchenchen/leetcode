# 28. Implement strStr()


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_needle = len(needle)
        if not needle:
            return 0

        for i in range(len(haystack) - len_needle + 1):
            if haystack[i:i+len_needle] == needle:
                return i

        return -1

    def strStr1(self, haystack, needle):
        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j] and needle[j] != "*":
                    break
                if j == len(needle) - 1:
                    return i
        return -1

print(Solution().strStr1("aaaaa", "bba"))