# 38. Count and Say

# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.
#
#
#
# Example 1:
#
# Input: 1
# Output: "1"
# Example 2:
#
# Input: 4
# Output: "1211"

# 思路：
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n - 1):
            cur, temp, count = s[0], '', 0
            for c in s:
                if cur == c:
                    count += 1
                else:
                    temp += str(count) + cur
                    cur = c
                    count = 1
            # don't forget the last combination
            temp += str(count) + cur
            s = temp
        return s
