# 30. Substring with Concatenation of All Words

# You are given a string, s, and a list of words, words, that are all of the same length.
# Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once
# and without any intervening characters.
#
# Example 1:
#
# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
# Example 2:
#
# Input:
#   s = "wordgoodstudentgoodword",
#   words = ["word","student"]
# Output: []

from collections import Counter, defaultdict
class Solution:
    def findSubstring(self, s, words):
        result = []
        if not words:
            return result

        counter, w_len = Counter(words), len(words[0])

        # sliding window(s)
        # 通过这样的方式保证range不越界, left window starts at i
        for i in range(w_len):
            left = i
            win_counter = defaultdict(int)
            count = 0
            # 找right window
            for j in range(i, len(s) - w_len + 1, w_len):
                tword = s[j:j + w_len]
                # valid word
                if tword in counter:
                    win_counter[tword] += 1
                    count += 1
                    # 用这个while loop处理一个window中的出现次数 > 在words中出现次数的word
                    while win_counter[tword] > counter[tword]:
                        win_counter[s[left:left + w_len]] -= 1
                        left += w_len
                        count -= 1
                    # window找到valid substring
                    if count == len(words):
                        result.append(left)
                # not valid, window中断
                else:
                    left = j + w_len
                    win_counter = {}
                    count = 0

        return result

print(Solution().findSubstring("barbarfoothefoobarman", ["foo","bar"]))