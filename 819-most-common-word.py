# 819. Most Common Word
# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
# It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
#
# Words in the list of banned words are given in lowercase, and free of punctuation.
# Words in the paragraph are not case sensitive.  The answer is in lowercase.
#
# Example:
# Input:
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.

import re
from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # words = re.sub("[!?',;.\s]+", " ", paragraph).lower().split()
        banned = set(banned)
        words = re.findall(r"\w+", paragraph.lower())
        # words = [word for word in words if word not in banned]
        words = filter(lambda x: x not in banned, words)
        word_count = defaultdict(int)
        max_count, cur = 0, None
        for word in words:
            word_count[word] += 1
            if word_count[word] > max_count:
                max_count = word_count[word]
                cur = word
        return cur
        # return max(word_count, key=lambda k: word_count[k])



