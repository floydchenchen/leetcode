# 249. Group Shifted Strings

# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd".
# We can keep "shifting" which forms the sequence:
#
# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets,
# group all strings that belong to the same shifting sequence.
#
# Example:
#
# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output:
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]

from collections import defaultdict
class Solution:
    def groupStrings(self, strings):
        groups = defaultdict(list)
        for s in strings:
            groups[tuple((ord(c) - ord(s[0])) % 26 for c in s)].append(s)
        return list(groups.values())

print(Solution().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
