# 686. Repeated String Match

# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it.
# If no such solution, return -1.
#
# For example, with A = "abcd" and B = "cdabcdab".
#
# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it;
# and B is not a substring of A repeated two times ("abcdabcd").

class Solution:
    # brute force
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        temp = ""
        count = 0
        while len(temp) < len(B):
            temp += A
            count += 1
            if B in temp:
                return count
        # 这几行是必要的，比如这种情况："abcd", "cdabcdab"
        temp += A
        if B in temp:
            return count + 1
        return -1