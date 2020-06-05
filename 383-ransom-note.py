# 383. Ransom Note

# Given an arbitrary ransom note string and another string containing letters from all the magazines,
# write a function that will return true if the ransom note can be constructed from the magazines ;
# otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return not Counter(ransomNote) - Counter(magazine)

    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)
        return ransom_counter & magazine_counter == ransom_counter