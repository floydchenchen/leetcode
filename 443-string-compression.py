# 443. String Compression

# Given an array of characters, compress it in-place.
#
# The compress_len after compression must always be smaller than or equal to the original array.
#
# Every element of the array should be a character (not int) of compress_len 1.
#
# After you are done modifying the input array in-place, return the new compress_len of the array.
#
#
# Follow up:
# Could you solve it using only O(1) extra space?
#
#
# Example 1:
# Input:
# ["a","a","b","b","c","c","c"]
#
# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
#
# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
# Example 2:
# Input:
# ["a"]
#
# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]
#
# Explanation:
# Nothing is replaced.
# Example 3:
# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
#
# Output:
# Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
#
# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
# Notice each digit has it's own entry in the array.


# 1. 必须要连续出现的char才会被compress
# 2. compress后面的数字可能会不只一位，这点需要考虑
# 3. 要更新compress的char和index
class Solution:
    def compress(self, chars):
        # left代表的是compress的pointer，代表着应该插入的index
        left = i = 0
        while i < len(chars):
            char, compress_len = chars[i], 1
            # 找到所有continuous char
            while (i + 1) < len(chars) and char == chars[i + 1]:
                compress_len, i = compress_len + 1, i + 1
            # 更新compress的char
            chars[left] = char
            # 如果compress_len，说明同时需要更新compress number
            if compress_len > 1:
                len_str = str(compress_len)
                chars[left + 1:left + 1 + len(len_str)] = len_str
                left += len(len_str)
            left, i = left + 1, i + 1
        return left

print(Solution().compress(["a","a","b","b","c","c","c"]))
