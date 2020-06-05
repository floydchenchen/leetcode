# 157. Read N Characters Given Read4

# The API: int read4(char *buf) reads 4 characters at a time from a file.
#
# The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
#
# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
#
# Example 1:
#
# Input: buf = "abc", n = 4
# Output: "abc"
# Explanation: The actual number of characters read is 3, which is "abc".
# 
# 
# Example 2:
#
# Input: buf = "abcde", n = 5
# Output: "abcde"

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
def read4(buf):
    pass

class Solution:
    def read(self, buf, n):
        idx = 0
        while True:
            buf4 = [""] * 4
            curr = min(read4(buf4), n - idx)  # curr is the number of chars that reads
            for i in range(curr):
                buf[idx] = buf4[i]
                idx += 1
            if curr != 4 or idx == n:  # return if it reaches the end of file or reaches n
                return idx