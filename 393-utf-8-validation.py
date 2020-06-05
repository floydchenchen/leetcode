# 393. UTF-8 Validation

# A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:
#
# For 1-byte character, the first bit is a 0, followed by its unicode code.
# For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes
# with most significant 2 bits being 10.
# This is how the UTF-8 encoding would work:
#
#    Char. number range  |        UTF-8 octet sequence
#       (hexadecimal)    |              (binary)
#    --------------------+---------------------------------------------
#    0000 0000-0000 007F | 0xxxxxxx
#    0000 0080-0000 07FF | 110xxxxx 10xxxxxx
#    0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
#    0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
# Given an array of integers representing the data, return whether it is a valid utf-8 encoding.
#
# Note:
# The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data.
# This means each integer represents only 1 byte of data.
#
# Example 1:
#
# data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.
#
# Return true.
# It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
# Example 2:
#
# data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.
#
# Return false.
# The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
# The next byte is a continuation byte which starts with 10 and that's correct.
# But the second continuation byte does not start with 10, so it is invalid.


# UTF-8 encoding rules: http://www.fileformat.info/info/unicode/utf8.htm

# expected = 0的时候，说明目前的byte满足要求
class Solution:
    def validUtf8(self, data):
        expected = 0
        for x in data:
            if expected == 0:
                # 0xxx xxxx
                if x >> 7 == 0:
                    expected = 0
                # x110 xxxx
                elif x >> 5 == int("110", 2):
                    expected = 1
                # 1110 xxxx
                elif x >> 4 == int("1110", 2):
                    expected = 2
                # 1111 0xxx
                elif x >> 3 == int("11110", 2):
                    expected = 3
                else:
                    return False
            else:
                # 10xx xxxx
                if x >> 6 == int("10", 2):
                    expected -= 1
                else:
                    return False
        return expected == 0


sol = Solution()
print(sol.validUtf8([197, 130, 1]))